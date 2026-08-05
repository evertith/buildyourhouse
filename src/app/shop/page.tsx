import type { Metadata } from 'next';
import React from 'react';
import CalloutBox from '@/components/CalloutBox';
import TrackedLink from '@/components/TrackedLink';
import SampleCapture from '@/components/SampleCapture';
import Icon, { type IconName } from '@/components/Icon';
import { generateProductSchema, generateFAQSchema, schemaToScriptTag } from '@/lib/schema';
import styles from './shop.module.css';

const STRIPE_CHECKOUT = 'https://buy.stripe.com/5kQ28racn54z0ReeZ5fAc00';
const SITE_URL = 'https://build-your-house.com';

export const metadata: Metadata = {
  alternates: { canonical: '/shop' },
  title: 'Owner-Builder Job Site Binder — 367 Pages of Templates & Checklists',
  description:
    'The complete owner-builder toolkit: 367 pages of contracts, checklists, inspection forms, and budget trackers, plus editable Word & Excel files. Print it, take it to the job site. $97 instant download.',
  keywords:
    'owner builder templates, construction checklists, job site binder, building contracts, owner builder tools',
  openGraph: {
    images: ['/binder/og-shop.jpg'],
  },
};

type BinderSection = {
  no: string;
  pages: string;
  title: string;
  items: string[];
  thumb: string;
  caption: string;
  alt: string;
};

const SECTIONS: BinderSection[] = [
  {
    no: 'SEC. 01',
    pages: '63 pages',
    title: 'Project Planning & Foundation',
    items: [
      'Master Project Timeline',
      'Budget Tracking Spreadsheet (Excel + PDF)',
      'Permit Application Checklist',
      'Site Preparation Checklist',
      'Foundation Checklist & Inspection Form',
      'Excavation & Backfill Log',
    ],
    thumb: '/binder/section-1-thumb.webp',
    caption: '1.5 Foundation Checklist',
    alt: 'Binder page 1.5, the Foundation Checklist: a printed inspection form with rows for footing depth, rebar size, and anchor bolt spacing.',
  },
  {
    no: 'SEC. 02',
    pages: '51 pages',
    title: 'Contracts & Legal Documents',
    items: [
      'Subcontractor Agreement (editable Word doc)',
      'Change Order Form',
      'Lien Waiver Templates',
      'Payment Draw Schedule',
      'Warranty Tracking & Material Delivery Receipts',
      'Safety Requirements & Dispute Resolution',
    ],
    thumb: '/binder/section-2-thumb.webp',
    caption: '2.1 Subcontractor Agreement',
    alt: 'Binder page 2.1, the Subcontractor Agreement: numbered contract clauses with blanks for scope of work, price, and payment schedule.',
  },
  {
    no: 'SEC. 03',
    pages: '53 pages',
    title: 'Rough-In Phase',
    items: [
      'Framing Inspection Checklist',
      'Electrical Rough-In Log',
      'Plumbing Rough-In Log',
      'HVAC Rough-In Guide',
      'Insulation & Air Sealing Guide',
    ],
    thumb: '/binder/section-3-thumb.webp',
    caption: '3.4 HVAC Rough-In Guide',
    alt: 'Binder page 3.4, the HVAC Rough-In Guide: a checklist of duct, line-set, and condensate items to verify before drywall goes up.',
  },
  {
    no: 'SEC. 04',
    pages: '57 pages',
    title: 'Systems Installation',
    items: [
      'Electrical System Completion Log',
      'Plumbing System Completion Log',
      'HVAC System Completion Log',
      'Final Systems Walkthrough',
    ],
    thumb: '/binder/section-4-thumb.webp',
    caption: '4.4 Final Systems Walkthrough',
    alt: 'Binder page 4.4, the Final Systems Walkthrough: a room-by-room sign-off sheet covering electrical, plumbing, and HVAC.',
  },
  {
    no: 'SEC. 05',
    pages: '51 pages',
    title: 'Finish Work',
    items: [
      'Drywall Completion Checklist',
      'Interior Door Installation Log',
      'Trim & Finish Carpentry Log',
      'Flooring Installation Guide',
      'Cabinet Installation Checklist',
      'Paint Color & Finish Tracking',
    ],
    thumb: '/binder/section-5-thumb.webp',
    caption: '5.1 Drywall Checklist',
    alt: 'Binder page 5.1, the Drywall Checklist: hang, tape, and finish items listed with columns for date and initials.',
  },
  {
    no: 'SEC. 06',
    pages: '45 pages',
    title: 'Daily Operations',
    items: [
      'Daily Job Site Log',
      'Weather Delay Log',
      'Material Delivery & Storage Log',
      'Tool & Equipment Log',
      'Safety Incident Report',
    ],
    thumb: '/binder/section-6-thumb.webp',
    caption: '6.1 Daily Job Site Log',
    alt: 'Binder page 6.1, the Daily Job Site Log: a one-page form with fields for crew on site, weather, deliveries, and delays.',
  },
  {
    no: 'SEC. 07',
    pages: '21 pages',
    title: 'Budget & Expenses',
    items: [
      'Expense Tracking Sheets (Excel + PDF)',
      'Receipt Organization System',
      'Cost Overrun Analysis',
      'Payment Tracking',
      'Final Budget Reconciliation',
    ],
    thumb: '/binder/section-7-thumb.webp',
    caption: '7.4 Payment Tracking',
    alt: 'Binder page 7.4, the Payment Tracking sheet: a ruled table of draws, invoices paid, and lien waivers received.',
  },
  {
    no: 'SEC. 08',
    pages: '20 pages',
    title: 'Quick Reference Guides',
    items: [
      'Residential Code Quick Reference (IRC highlights)',
      'Lumber Span Tables',
      'Material Calculators (concrete, drywall, paint, roofing)',
      'Emergency Contacts Sheet',
      'Common Measurement Conversions',
    ],
    thumb: '/binder/section-8-thumb.webp',
    caption: '8.2 Span Tables',
    alt: 'Binder page 8.2, the Span Tables: floor joist spans by species and size, with the IRC 2021 table number printed above the grid.',
  },
];

const SAMPLES: { src: string; caption: string; alt: string }[] = [
  {
    src: '/binder/spans-large.webp',
    caption: '8.2 Span Tables — IRC 2021 values',
    alt: 'Full page of the 8.2 Span Tables: allowable floor joist spans by lumber species, size, and spacing, with the IRC 2021 table number printed above the grid.',
  },
  {
    src: '/binder/contract-large.webp',
    caption: '2.1 Subcontractor Agreement',
    alt: 'Full page of the 2.1 Subcontractor Agreement: numbered contract clauses with blanks for scope of work, price, payment schedule, and signatures.',
  },
  {
    src: '/binder/budget-large.webp',
    caption: '1.2 Budget Tracking',
    alt: 'Full page of the 1.2 Budget Tracking sheet: cost categories down the left with estimate, actual, and variance columns across the page.',
  },
];

const STEPS: { no: string; title: string; copy: string }[] = [
  {
    no: 'Step 01',
    title: 'Purchase & Download',
    copy: 'Instant access to the complete ZIP file with all 367 pages of templates, checklists, and forms.',
  },
  {
    no: 'Step 02',
    title: 'Print & Organize',
    copy: 'Follow the included “How to Use This Binder” guide to print and assemble your binder. Takes about 2 hours.',
  },
  {
    no: 'Step 03',
    title: 'Take to Job Site',
    copy: 'Show up organized and professional. Everything you need at your fingertips — no phone required.',
  },
  {
    no: 'Step 04',
    title: 'Build With Confidence',
    copy: 'Use the checklists, templates, and forms throughout your build. Never miss a critical step again.',
  },
];

const INCLUDES: string[] = [
  '367 pages of templates, checklists, and forms (Second Edition, revised 2026)',
  '8 comprehensive sections covering every phase',
  '57 print-ready PDFs optimized for 3-ring binders',
  'Editable Word & Excel files for customization',
  'Material calculators & quick-reference tables',
  '“How to Use This Binder” assembly guide',
  'Lifetime access to all files',
  'Free updates when we add new content',
];

const GUARANTEES: { icon: IconName; label: string; copy: string }[] = [
  { icon: 'lock', label: 'Secure checkout', copy: 'Powered by Stripe — your payment details never touch this site.' },
  { icon: 'bolt', label: 'Instant access', copy: 'Download the moment your payment goes through.' },
  { icon: 'check', label: 'Lifetime access', copy: 'Your files don’t expire — recover your download anytime with your purchase email.' },
];

// `answer` feeds the FAQPage schema, so it stays plain text. `node` is the
// rendered version when an answer needs a link.
type Faq = { question: string; answer: string; node?: React.ReactNode };

const FAQS: Faq[] = [
  {
    question: 'Do I need special equipment to print this?',
    answer:
      'No. Any standard printer works. You can print at home or take the PDF files to an office supply store (Staples, Office Depot, FedEx Office). Expect to spend $40-60 for printing and binding.',
  },
  {
    question: 'Can I customize the templates?',
    answer:
      'Yes! Contract templates and tracking sheets come as editable Word and Excel files. Customize them with your project details, add your logo, or modify to fit your needs.',
  },
  {
    question: 'Is this legal in my state?',
    answer:
      'The templates are general-purpose construction documents used nationwide. However, always verify contracts with a local attorney and ensure compliance with your state’s building codes and regulations.',
  },
  {
    question: 'Do you offer updates?',
    answer:
      'Yes! When we add new templates or update existing ones, you’ll get free access to download the latest version. Your purchase includes lifetime access to all updates.',
  },
  {
    question: 'What if I have questions while using the binder?',
    answer:
      'Browse our free guides on Build Your House for detailed explanations of each construction phase. The website has hundreds of pages of owner-builder advice to complement the binder system.',
  },
  {
    question: 'Can I share this with my spouse or partner?',
    answer:
      'Absolutely! Use it for your personal owner-builder project. Please don’t distribute or resell the files, but printing multiple copies for your own build is perfectly fine.',
  },
  {
    question: 'What format are the files in?',
    answer:
      'PDFs for printing, Word docs (.docx) for contracts and letters, Excel spreadsheets (.xlsx) for budgets and calculators. Everything works on Windows and Mac.',
  },
  {
    question: 'How soon can I download this?',
    answer:
      'Immediately. As soon as your payment goes through, you’re taken straight to your download page — no waiting, no shipping. Lose the page later? Recover your download anytime at build-your-house.com/shop/recover using your purchase email.',
    node: (
      <>
        Immediately. As soon as your payment goes through, you’re taken straight to your download
        page — no waiting, no shipping. Lose the page later? Recover your download anytime at{' '}
        <a href="/shop/recover">build-your-house.com/shop/recover</a> using your purchase email.
      </>
    ),
  },
];

const productSchema = generateProductSchema({
  name: 'The Owner-Builder Job Site Binder',
  description:
    'A 367-page printed system for owner-builders: 57 print-ready PDF contracts, checklists, inspection forms, and logs across 8 sections, plus editable Word contracts and auto-calculating Excel budget workbooks. Second Edition, revised 2026.',
  image: `${SITE_URL}/binder/og-shop.jpg`,
  url: `${SITE_URL}/shop`,
  price: 97,
  priceCurrency: 'USD',
  availability: 'InStock',
  brand: 'Build Your House',
});

const faqSchema = generateFAQSchema(
  FAQS.map(({ question, answer }) => ({ question, answer }))
);

export default function JobSiteBinder() {
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
              <div className={`${styles.eyebrow} bp-eyebrow`}>Second Edition · Revised 2026</div>
              <h1 className={styles.heroTitle}>The Owner-Builder Job Site Binder</h1>
              <p className={styles.heroSub}>
                Every contract, checklist, and form for your build.
              </p>

              <div className={styles.dimstrip}>
                <div className={styles.dimcell}>
                  <span className={styles.k}>Pages</span>
                  <span className={styles.v}>367</span>
                </div>
                <div className={styles.dimcell}>
                  <span className={styles.k}>Sections</span>
                  <span className={styles.v}>08</span>
                </div>
                <div className={styles.dimcell}>
                  <span className={styles.k}>PDFs</span>
                  <span className={styles.v}>57</span>
                </div>
                <div className={styles.dimcell}>
                  <span className={styles.k}>Editable</span>
                  <span className={styles.v}>12</span>
                </div>
              </div>

              <div className={styles.heroCtas}>
                <TrackedLink
                  href={STRIPE_CHECKOUT}
                  eventName="begin_checkout"
                  eventParams={{
                    currency: 'USD',
                    value: 97,
                    item_name: 'job_site_binder',
                    location: 'hero',
                  }}
                  className={styles.btnPrimary}
                >
                  Get instant access — $97
                </TrackedLink>
                <TrackedLink
                  href="#inside"
                  eventName="shop_cta_click"
                  eventParams={{ location: 'hero_see_inside' }}
                  className={styles.btnGhost}
                >
                  See what’s inside ↓
                </TrackedLink>
              </div>
              <p className={styles.heroFine}>
                One-time payment · Instant download
              </p>
            </div>

            <div className={styles.stack}>
              {/* Thumbnails, not the 1200px versions: only the paper edge shows here. */}
              <img
                src="/binder/section-2-thumb.webp"
                alt="A page of the Subcontractor Agreement stacked behind the binder cover."
                width={400}
                height={518}
                className={`${styles.sheet} ${styles.sheetDark} ${styles.stackBack} ${styles.stackBack2}`}
              />
              <img
                src="/binder/section-8-thumb.webp"
                alt="A page of the lumber span tables stacked behind the binder cover."
                width={400}
                height={518}
                className={`${styles.sheet} ${styles.sheetDark} ${styles.stackBack} ${styles.stackBack1}`}
              />
              <img
                src="/binder/cover-hero.webp"
                alt="Cover of the Owner-Builder Job Site Binder, Second Edition."
                width={900}
                height={1165}
                className={`${styles.sheet} ${styles.sheetDark} ${styles.stackFront}`}
              />
            </div>
          </div>
        </div>
      </section>

      {/* ---------- WHY PAPER ---------- */}
      <section className={styles.block}>
        <div className={styles.wrap}>
          <div className={styles.secHead}>
            <div>
              <div className={styles.secLabel}>Why paper</div>
              <h2 className={styles.secTitle}>A job site eats phones.</h2>
            </div>
            <div className={styles.secMeta}>
              Second Edition
              <br />
              Revised 2026
            </div>
          </div>
          <p className={styles.lead}>
            Gloves, dust, dead batteries, and no signal — a build site is hostile to the device
            your paperwork lives on. Paper isn’t: you can hand a sub the exact page they need,
            mark up a checklist while the inspector watches, and leave the whole thing in the truck
            without worrying about the charge. This is that system, printed — 367 pages of the
            contracts, checklists, and logs a build actually generates.
          </p>
        </div>
      </section>

      {/* ---------- WHAT'S INSIDE ---------- */}
      <section id="inside" className={`${styles.block} ${styles.anchor}`}>
        <div className={styles.wrap}>
          <div className={styles.secHead}>
            <div>
              <div className={styles.secLabel}>Contents</div>
              <h2 className={styles.secTitle}>Eight sections, 367 pages</h2>
            </div>
            <div className={styles.secMeta}>
              57 print-ready PDFs
              <br />
              12 editable files
            </div>
          </div>

          <div className={styles.index}>
            {SECTIONS.map((s) => (
              <div key={s.no} className={styles.row}>
                <div className={styles.rowNo}>
                  {s.no}
                  <span className={styles.rowPages}>{s.pages}</span>
                </div>
                <div>
                  <h3 className={styles.rowTitle}>{s.title}</h3>
                  <ul className={styles.rowList}>
                    {s.items.map((item) => (
                      <li key={item}>{item}</li>
                    ))}
                  </ul>
                </div>
                <figure className={styles.rowFig}>
                  <img
                    src={s.thumb}
                    alt={s.alt}
                    width={400}
                    height={518}
                    loading="lazy"
                    className={styles.sheet}
                  />
                  <figcaption className={styles.sheetCap}>{s.caption}</figcaption>
                </figure>
              </div>
            ))}

            {/* Makes the page column add up to 367 for anyone who checks. */}
            <div className={`${styles.row} ${styles.rowQuiet}`}>
              <div className={styles.rowNo}>
                FRONT MATTER
                <span className={styles.rowPages}>6 pages</span>
              </div>
              <p className={styles.rowQuietCopy}>
                Cover · spine labels · how-to guide · contents
              </p>
              <span />
            </div>
          </div>
        </div>
      </section>

      {/* ---------- LOOK INSIDE ---------- */}
      <div className={styles.lookBand}>
        <div className={styles.wrap}>
          <div className={styles.secHead}>
            <div>
              <div className={styles.secLabel}>Sample sheets</div>
              <h2 className={styles.secTitle}>Three pages, full size</h2>
            </div>
            <div className={styles.secMeta}>
              Actual pages
              <br />
              No watermarks
            </div>
          </div>
          <div className={styles.samples}>
            {SAMPLES.map((s) => (
              <figure key={s.src} className={styles.sampleFig}>
                <img
                  src={s.src}
                  alt={s.alt}
                  width={1200}
                  height={1553}
                  loading="lazy"
                  className={styles.sheet}
                />
                <figcaption className={styles.sheetCap}>{s.caption}</figcaption>
              </figure>
            ))}
          </div>
        </div>
      </div>

      {/* ---------- EDITABLE FILES ---------- */}
      <section className={styles.block}>
        <div className={styles.wrap}>
          <div className={styles.secHead}>
            <div>
              <div className={styles.secLabel}>Editable files</div>
              <h2 className={styles.secTitle}>The trackers do the math</h2>
            </div>
            <div className={styles.secMeta}>
              12 files
              <br />
              .docx + .xlsx
            </div>
          </div>

          <div className={styles.editable}>
            <figure className={styles.sampleFig}>
              <img
                src="/binder/excel-budget.webp"
                alt="The budget workbook open in a spreadsheet: cost categories down the left with estimated cost, actual cost, variance, and vendor columns across, and subtotals filled in by formula."
                width={1100}
                height={605}
                loading="lazy"
                className={`${styles.sheet} ${styles.sheetWide}`}
              />
              <figcaption className={styles.sheetCap}>Budget workbook — live formulas</figcaption>
            </figure>

            <div className={styles.editableCopy}>
              <p>
                <span className={styles.fileTag}>.docx</span> — contract templates you customize
                with your own project details. Subcontractor agreements, change orders, and lien
                waivers, with the blanks left where your scope, price, and dates go.
              </p>
              <p>
                <span className={styles.fileTag}>.xlsx</span> — budget, expense, and payment
                trackers where every <strong>Variance</strong>, <strong>Subtotal</strong>, and
                running-total cell is a live formula. Type in what you actually paid and the
                overrun calculates itself.
              </p>
              <p>
                Everything opens in Microsoft Office, Google Sheets, or LibreOffice. The same
                documents are in the binder as print-ready PDFs, so you can work either way.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* ---------- BEFORE YOU BUY ---------- */}
      <section className={styles.block}>
        <div className={styles.wrap}>
          <div className={styles.secHead}>
            <div>
              <div className={styles.secLabel}>Before you buy</div>
              <h2 className={styles.secTitle}>
                Nothing to review yet. Here’s what you can check instead.
              </h2>
            </div>
            <div className={styles.secMeta}>
              No reviews yet
              <br />
              Check it yourself
            </div>
          </div>

          <div className={styles.trust}>
            <div className={styles.trustItem}>
              <Icon name="doc" size={26} className={styles.trustIco} />
              <div>
                <p className={styles.trustLabel}>Read 19 pages before you pay</p>
                <p className={styles.trustCopy}>
                  The free sample is 19 real pages lifted straight out of the binder: the cover,
                  the full 1.5 Foundation Checklist, and the complete 8.2 Span Tables. Same
                  typesetting, same page size, no watermark. If the sample isn’t worth printing,
                  neither is the rest.
                </p>
                <SampleCapture />
              </div>
            </div>

            <div className={styles.trustItem}>
              <Icon name="ruler" size={26} className={styles.trustIco} />
              <div>
                <p className={styles.trustLabel}>Check the numbers yourself</p>
                <p className={styles.trustCopy}>
                  The span tables are transcribed from IRC 2021, and every table prints its source
                  number on the page. Look up the table it cites and compare it line by line — if a
                  number is wrong, you’ll find it in about a minute. That is the point of printing
                  the citation.
                </p>
                <figure className={styles.ircFig}>
                  <img
                    src="/binder/irc-citation-zoom.webp"
                    alt="Close crop of a binder page showing the printed source line: IRC Table R502.3.1(2)."
                    width={640}
                    height={143}
                    loading="lazy"
                    className={`${styles.sheet} ${styles.sheetWide}`}
                  />
                  <figcaption className={styles.sheetCap}>
                    Detail — source citation printed on the page
                  </figcaption>
                </figure>
              </div>
            </div>

            <div className={styles.trustItem}>
              <Icon name="compass" size={26} className={styles.trustIco} />
              <div>
                <p className={styles.trustLabel}>You already know who wrote it</p>
                <p className={styles.trustCopy}>
                  This is the shop attached to Build Your House — the same site that publishes free
                  owner-builder permitting guides for all 50 states. Read a few of those before you
                  spend anything. The binder is the same work, printed and organized.
                </p>
                <a className={styles.trustLink} href="/permitting/state-guides">
                  Browse the 50 state guides <span aria-hidden="true">→</span>
                </a>
              </div>
            </div>

          </div>
        </div>
      </section>

      {/* ---------- HOW IT WORKS ---------- */}
      <section className={styles.block}>
        <div className={styles.wrap}>
          <div className={styles.secHead}>
            <div>
              <div className={styles.secLabel}>Assembly</div>
              <h2 className={styles.secTitle}>From download to job site</h2>
            </div>
            <div className={styles.secMeta}>
              About 2 hours
              <br />
              $40–60 to print
            </div>
          </div>

          <div className={styles.steps}>
            {STEPS.map((s) => (
              <div key={s.no} className={styles.step}>
                <span className={styles.stepNo}>{s.no}</span>
                <h3 className={styles.stepTitle}>{s.title}</h3>
                <p className={styles.stepCopy}>{s.copy}</p>
              </div>
            ))}
          </div>

          <CalloutBox type="info" title="Printing cost">
            Expect to spend $40-60 at an office supply store for printing and binding. Print
            double-sided to save paper and money.
          </CalloutBox>
        </div>
      </section>

      {/* ---------- ORDER ---------- */}
      <section id="purchase" className={`${styles.block} ${styles.anchor}`}>
        <div className={styles.wrap}>
          <div className={styles.secHead}>
            <div>
              <div className={styles.secLabel}>Order</div>
              <h2 className={styles.secTitle}>Get the binder</h2>
            </div>
            <div className={styles.secMeta}>
              One-time
              <br />
              Instant download
            </div>
          </div>

          <div className={styles.order}>
            <div className={styles.orderNo}>
              <span className="bp-sheet-no">Job Site Binder</span>
              <span>Second Ed. · Rev. 2026</span>
            </div>

            <h3 className={styles.orderTitle}>The Complete Owner-Builder Job Site Binder System</h3>

            <p className={`${styles.inclLabel} bp-mono-label`}>What you get</p>
            <ul className={styles.incl}>
              {INCLUDES.map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>

            <div className={styles.priceRow}>
              <span className={styles.priceKey}>Price</span>
              <span className={styles.leader} aria-hidden="true" />
              <span className={styles.priceVal}>$97</span>
            </div>
            <div className={`${styles.orderDim} bp-dimline`}>
              One-time · Instant download
            </div>

            <TrackedLink
              href={STRIPE_CHECKOUT}
              eventName="begin_checkout"
              eventParams={{
                currency: 'USD',
                value: 97,
                item_name: 'job_site_binder',
                location: 'purchase_box',
              }}
              className={`${styles.btnPrimary} ${styles.orderCta}`}
            >
              Get instant access — $97
            </TrackedLink>

            <div className={styles.guarantees}>
              {GUARANTEES.map((g) => (
                <div key={g.label} className={styles.guarantee}>
                  <Icon name={g.icon} size={22} className={styles.guaranteeIco} />
                  <div>
                    <span className={styles.guaranteeLabel}>{g.label}</span>
                    <p>{g.copy}</p>
                  </div>
                </div>
              ))}
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
                <p className={styles.faqA}>{f.node ?? f.answer}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ---------- FINAL CTA ---------- */}
      <section className={`${styles.finalCta} bp-band bp-grid`}>
        <div className={styles.ctaInner}>
          <div className={`${styles.eyebrow} bp-eyebrow`}>367 pages · 8 sections · $97</div>
          <h2 className={styles.ctaTitle}>Print it once. Use it for the whole build.</h2>
          <p className={styles.ctaSub}>
            The complete binder downloads the moment your payment clears — every contract,
            checklist, and log, ready for the printer.
          </p>
          <div className={styles.heroCtas}>
            <TrackedLink
              href={STRIPE_CHECKOUT}
              eventName="begin_checkout"
              eventParams={{
                currency: 'USD',
                value: 97,
                item_name: 'job_site_binder',
                location: 'final',
              }}
              className={styles.btnPrimary}
            >
              Get instant access — $97
            </TrackedLink>
          </div>
          <p className={styles.heroFine}>
            One-time payment · Instant download
          </p>
        </div>
      </section>
    </div>
  );
}
