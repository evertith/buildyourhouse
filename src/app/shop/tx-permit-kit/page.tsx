import type { Metadata } from 'next';
import BinderCTA from '@/components/BinderCTA';
import TrackedLink from '@/components/TrackedLink';
import Icon, { type IconName } from '@/components/Icon';
import { generateProductSchema, generateFAQSchema, schemaToScriptTag } from '@/lib/schema';
import styles from '../product.module.css';

// filled in after /admin/api/provision-products creates the payment link
const STRIPE_CHECKOUT = 'https://buy.stripe.com/aFaeVd4S3dB5dE004bfAc06';
const SITE_URL = 'https://build-your-house.com';
const PRICE = 34;

export const metadata: Metadata = {
  alternates: { canonical: '/shop/tx-permit-kit' },
  title: 'Texas Owner-Builder Permit Kit — $34',
  description:
    'Every rule Texas actually applies to an owner-builder: no state contractor license and no state building permit — but licensed trades, TCEQ septic, a statewide energy code, and coastal windstorm certification bind you anyway. Two-track permit checklist (city and unincorporated county), inspection sequences, and where-to-file directory. 33 print-ready pages with the statute citations on the page. $34 instant download.',
  keywords:
    'Texas owner builder permit, can you build your own house in Texas, Texas building permit requirements, owner builder exemption Texas, Texas septic permit new construction, Texas windstorm certificate WPI-1, unincorporated county building Texas',
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
    no: 'TX.0',
    pages: '3 pages',
    title: 'Cover & How to Use',
    copy:
      'What is in the kit, the one question that decides everything — is the lot inside a city’s limits or not — and what order to work through the documents on whichever track you are on.',
  },
  {
    no: 'TX.1',
    pages: '8 pages',
    title: 'The Owner-Builder’s Legal Position in Texas',
    copy:
      'Texas licenses no general contractors and issues no state building permit — printed as an as-of-August-2026 fact with the proof cited. Then the part that trips people: the three licensed trades, each homeowner exemption quoted verbatim with its trap flagged, the city registration and homeowner-permit practices layered on top, and the water-well carve-out. Occupations Code Chapters 1305, 1301, and 1302 on the page.',
    thumb: '/binder/txk-exempt.webp',
    caption: 'TX.1 The legal position',
    alt: 'Page TX.1, The Owner-Builder’s Legal Position in Texas: the no-state-license, no-state-permit finding with the print-date warning callout and Occupations Code citations.',
  },
  {
    no: 'TX.2',
    pages: '9 pages',
    title: 'Permit Application Checklist',
    copy:
      'Two tracks. Inside a city: the IRC-based municipal code, the plan set, registrations, and the 45-day action clock the city owes you (Local Gov’t Code § 214.904). Unincorporated: no building permit exists — the checklist covers the septic permit, floodplain permit, energy-code compliance, windstorm notice, and driveway permit that do, plus the homestead lien rules for every sub you hire: written contract before work, both spouses, filed with the county clerk.',
    thumb: '/binder/txk-checklist.webp',
    caption: 'TX.2 Application checklist',
    alt: 'Page TX.2, the Permit Application Checklist: the two-track checklist with checkboxes for city and unincorporated-county builds.',
  },
  {
    no: 'TX.3',
    pages: '5 pages',
    title: 'Inspection Sequence',
    copy:
      'Inside a city: the inspection ladder from temporary power through the Certificate of Occupancy, keyed to published city lists. Outside one: there is no ladder — five separate inspectors, from the septic inspection to the utility’s meter release, and the gaps where nobody inspects at all.',
    thumb: '/binder/txk-inspect.webp',
    caption: 'TX.3 Inspection sequence',
    alt: 'Page TX.3, the Inspection Sequence: the municipal inspection ladder and the county-track inspection points, with what each inspector looks at.',
  },
  {
    no: 'TX.4',
    pages: '5 pages',
    title: 'Where-to-File Directory',
    copy:
      'How to pin down whether your lot sits in a city, its ETJ, or the unincorporated county — then which office owns each piece: TDLR, TSBPE, TCEQ, TDI windstorm, SECO, TxDOT, and the high-volume city and county permit offices, with a page to record what you confirmed.',
  },
  {
    no: 'TX.5',
    pages: '3 pages',
    title: 'Forms & Documents Index',
    copy:
      'Every named form in the kit — TCEQ 0235 for septic, TDI’s WPI-1, TxDOT Form 1058, the ESL energy self-certification, the city homestead affidavits — with its official name and the office that issues it, so you can pull a current copy yourself.',
  },
];

const INCLUDES: string[] = [
  '33 print-ready pages across 6 documents, letter size',
  'The owner-builder legal position: the trades, the three exemptions, the traps (Occupations Code Chs. 1305, 1301, 1302)',
  'A two-track permit application checklist — city hall and unincorporated county',
  'Both inspection sequences: the municipal ladder and the county’s five separate inspectors',
  'Where-to-file directory: TDLR, TSBPE, TCEQ, TDI windstorm, SECO, TxDOT, and the big-city portals',
  'Statute and code citations printed on the page, not linked away',
  'Lifetime access — re-download anytime with your purchase email',
];

const KNOWS: { icon: IconName; label: string; copy: string }[] = [
  {
    icon: 'bolt',
    label: 'The electrical exemption says “owns and resides in” — a new build may not qualify',
    copy:
      'The homeowner exemption in Occupations Code § 1305.003(a)(6) covers electrical work on a dwelling the person “owns and resides in” — and a house under construction is a dwelling you do not yet reside in. TDLR has published no interpretation for new construction, and a city ordinance can take the exemption away entirely, the way Houston’s does. The kit prints the exemption verbatim, flags the gap, and gives you the safe plays: hire a licensed electrician, or put the question to TDLR in writing before you rely on it.',
  },
  {
    icon: 'permit',
    label: 'Outside city limits, the septic permit is the building permit',
    copy:
      'Counties generally cannot require a building permit for a single-family house — but you must hold a permit and an approved plan before constructing a septic system (Health & Safety Code § 366.051). That makes the OSSF permit the document that actually gates construction on most unincorporated lots, with a site evaluation first and an inspection before the system is covered. Guides that say “the county has no permits” also walk people past the floodplain development permit, where violations are a Class C misdemeanor and each day is a separate offense (Water Code § 16.3221). The kit sequences all of it.',
  },
  {
    icon: 'doc',
    label: 'The energy code applies even where no permit office exists',
    copy:
      'Health & Safety Code § 388.004 is the statute nobody expects: outside a city’s jurisdiction your house must still comply with the state energy code — the energy chapter of the 2015 IRC as of August 2026 — and the statute names exactly three ways to show it: an accredited efficiency program, a private code-certified inspector, or the builder’s own certification on the Energy Systems Laboratory form. The builder keeps the documentation for three years and gives the owner a copy. The kit prints the three routes verbatim and puts the form in the county-track checklist.',
  },
  {
    icon: 'check',
    label: 'On the coast, the windstorm notice comes before construction',
    copy:
      'In the 14 first-tier coastal counties and parts of Harris County east of SH 146, a house built outside TDI’s windstorm paper trail may not be insurable through TWIA. The WPI-1 notice of intent is filed before construction begins (Insurance Code § 2210.2515(b)), inspections or an engineer’s certification follow during the build, and the WPI-8 certificate at the end is the evidence of insurability (§ 2210.251). Skipping the notice and shopping for windstorm coverage after the fact is the classic coastal owner-builder disaster. The kit sequences the windstorm steps with the rest of the track.',
  },
];

type Faq = { question: string; answer: string };

const FAQS: Faq[] = [
  {
    question: 'Can you build your own house in Texas?',
    answer:
      'Yes. As of August 2026 no Texas state agency issues a general contractor or home-builder license — TDLR’s list of regulated programs has no such program, and the Texas Residential Construction Commission’s statute expired in 2009 — so anyone, including you, can act as their own builder. What Texas does license is the trades: electrical, plumbing, and HVAC work each require a state license under Occupations Code Chapters 1305, 1301, and 1302, with homeowner exemptions worded differently for each one. Some cities also require anyone pulling permits to register with the permit office first. The kit walks each rule with the citation printed beside it.',
  },
  {
    question: 'Do you need a permit to build a house in Texas?',
    answer:
      'It depends on one question: is the lot inside a city’s limits? Inside a city, yes — state law adopts the International Residential Code as the municipal residential building code (Local Government Code § 214.212), the city issues the permit, and it must act on your application within 45 days (§ 214.904). In the unincorporated county there is no building permit — counties generally cannot require one for a single-family house (§ 233.153(d)(1)) — but the septic permit, the floodplain development permit, the statewide energy code, and, on the coast, windstorm certification apply instead. The kit’s checklist runs both tracks.',
  },
  {
    question: 'Is there an owner-builder opt-out in Texas?',
    answer:
      'There is nothing to opt out of at the state level — Texas has no contractor license and no state building permit, so no statewide owner-builder exemption form exists. What the phrase usually points at is city practice: cities that require contractor registration often let an owner-occupant pull permits personally instead. Fort Worth uses a Homestead Permit Affidavit; San Antonio issues a homeowner’s permit after you attest you will own and occupy or rent the home for 12 months after completion and take responsibility for all inspections; Houston lets a homeowner pull the plumbing permit (form CE1284) but issues electrical permits only to licensed master electricians. The kit’s rule: ask your permit office in writing whether the owner-occupant may pull each permit personally, and which trades are excluded.',
  },
  {
    question: 'Can I do my own electrical and plumbing work in Texas?',
    answer:
      'Each trade has its own exemption, and the wording is the trap. Plumbing: a property owner needs no license to perform plumbing in their own homestead (Occupations Code § 1301.051) — one sentence, no occupancy conditions, though for a not-yet-occupied new build the kit tells you to confirm the homestead question with the plumbing board. Electrical: the exemption covers work on a dwelling the person “owns and resides in” (§ 1305.003(a)(6)) — a new house you do not yet live in is not clearly covered, and a city ordinance can remove the exemption entirely, as Houston’s does. HVAC: the exemption covers a building “owned solely by the person as the person’s home” (§ 1302.053), which raises its own questions on jointly titled property. The kit quotes all three verbatim and flags each trap.',
  },
  {
    question: 'Do I need a septic permit before I start building?',
    answer:
      'Yes — and outside city limits it functions as the de facto building permit. Texas requires a permit and an approved plan before you construct or operate an on-site sewage facility (Health & Safety Code § 366.051), issued by the county as TCEQ’s authorized agent, or by TCEQ directly where no agent exists, with a site evaluation first. There is a narrow exemption for a single residence on a tract of ten acres or more, with the disposal lines at least 100 feet from the property line and effluent kept on the property (§ 366.052) — it is precise, and most lots do not qualify. The kit puts the septic clock at the front of the county track, where it belongs.',
  },
  {
    question: 'Do I need windstorm certification to build in Texas?',
    answer:
      'Only in the designated catastrophe area: the 14 first-tier coastal counties plus parts of Harris County east of State Highway 146. There, if you ever want windstorm coverage through TWIA, you file TDI’s WPI-1 notice of intent before construction begins (Insurance Code § 2210.2515(b)), have the work engineer-certified or inspected during construction, and receive a WPI-8 or WPI-8-E certificate — the document that serves as evidence the house is insurable (§ 2210.251). Building first and asking about windstorm insurance later is the classic coastal owner-builder disaster. Inland, none of this applies, and the kit says so plainly.',
  },
];

const productSchema = generateProductSchema({
  name: 'Texas Owner-Builder Permit Kit',
  description:
    'Texas owner-builder permitting, start to finish: the owner-builder legal position (no state license, no state permit — and the trade, septic, energy, and windstorm rules that bind anyway), the two-track permit application checklist, inspection sequences for city and county, where-to-file directory, and forms index. 33 print-ready pages across 6 documents, with the statute and code citations printed on the page. Verified against statutes.capitol.texas.gov, TDLR, TCEQ, TDI, and city permitting sources, August 2026.',
  image: `${SITE_URL}/binder/og-shop.jpg`,
  url: `${SITE_URL}/shop/tx-permit-kit`,
  price: PRICE,
  priceCurrency: 'USD',
  availability: 'InStock',
  brand: 'Build Your House',
  sku: 'tx-permit-kit',
});

const faqSchema = generateFAQSchema(FAQS);

export default function TXPermitKit() {
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
                Texas · Permit Kit
              </div>
              <h1 className={styles.heroTitle}>Texas Owner-Builder Permit Kit</h1>
              <p className={styles.heroSub}>
                No state contractor license and no state building permit — and the trade-licensing,
                septic, energy-code, and windstorm rules that bind you anyway. Both tracks, city
                and county, verified against the statutes with the citations printed on the page.
              </p>

              <div className={styles.dimstrip}>
                <div className={styles.dimcell}>
                  <span className={styles.k}>Pages</span>
                  <span className={styles.v}>33</span>
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
                    item_name: 'tx-permit-kit',
                    location: 'hero',
                  }}
                  className={styles.btnPrimary}
                >
                  Get the kit — ${PRICE}
                </TrackedLink>
                <TrackedLink
                  href="#contents"
                  eventName="shop_cta_click"
                  eventParams={{ location: 'txk_hero_see_inside', item_name: 'tx-permit-kit' }}
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
                  eventParams={{ location: 'txk_hero_family', context: 'tx-permit-kit' }}
                  className={styles.familyLink}
                >
                  Job Site Binder family
                </TrackedLink>
              </p>
            </div>

            <div className={styles.stack}>
              <img
                src="/binder/txk-checklist.webp"
                alt="A page of the Texas two-track permit checklist stacked behind the legal-position walkthrough."
                width={700}
                height={906}
                className={`${styles.sheet} ${styles.sheetDark} ${styles.stackBack}`}
              />
              <img
                src="/binder/txk-exempt.webp"
                alt="The Texas owner-builder legal-position document, page TX.1 of the permit kit."
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
              <h2 className={styles.secTitle}>Six documents, 33 pages</h2>
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
            Four things in this kit that most Texas owner-builder advice gets wrong. Each one is
            checkable in a couple of minutes — which is the point of printing the citation. If you
            want the lay of the land first, the free{' '}
            <TrackedLink
              href="/permitting/state-guides/texas"
              eventName="shop_cta_click"
              eventParams={{ location: 'txk_knows_state_guide', context: 'tx-permit-kit' }}
            >
              Texas owner-builder guide
            </TrackedLink>{' '}
            covers it; the kit is the working version.
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
            Verified against statutes.capitol.texas.gov, TDLR, TCEQ, TDI, and city permitting
            sources, August 2026 · Citations printed on each page
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
              <span className="bp-sheet-no">TX Permit Kit</span>
              <span>Rev. August 2026</span>
            </div>

            <h3 className={styles.orderTitle}>
              The Texas Owner-Builder Permit Kit
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
                item_name: 'tx-permit-kit',
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
                Statutes and code editions change, and Texas cities amend everything locally.
                Confirm each rule with your city or county — the kit prints its sources so you can.
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
          <p className={styles.lead}>
            Building in a different state? The same six documents exist for{' '}
            <TrackedLink
              href="/shop/nc-permit-kit"
              eventName="shop_cta_click"
              eventParams={{ location: 'txk_crosssell_nc', context: 'tx-permit-kit' }}
            >
              North Carolina
            </TrackedLink>
            ,{' '}
            <TrackedLink
              href="/shop/ga-permit-kit"
              eventName="shop_cta_click"
              eventParams={{ location: 'txk_crosssell_ga', context: 'tx-permit-kit' }}
            >
              Georgia
            </TrackedLink>
            , and{' '}
            <TrackedLink
              href="/shop/va-permit-kit"
              eventName="shop_cta_click"
              eventParams={{ location: 'txk_crosssell_va', context: 'tx-permit-kit' }}
            >
              Virginia
            </TrackedLink>
            .
          </p>
          <BinderCTA
            context="tx-permit-kit"
            lead="The kit gets your permits. The binder runs the build — 367 pages of contracts, inspection forms, daily logs, and budget trackers covering every phase from footing to final, in the same print-and-go format."
          />
        </div>
      </section>
    </div>
  );
}
