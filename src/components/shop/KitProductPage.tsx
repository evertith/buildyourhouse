import BinderCTA from '@/components/BinderCTA';
import TrackedLink from '@/components/TrackedLink';
import Icon from '@/components/Icon';
import { kitBySlug, shippedKits } from '@/lib/kits';
import { KIT_PRICE, countWord, dim, type KitContent } from '@/lib/kit-content';
import { generateProductSchema, generateFAQSchema, schemaToScriptTag } from '@/lib/schema';
import styles from '@/app/shop/product.module.css';

const SITE_URL = 'https://build-your-house.com';

const BINDER_LEAD =
  'The kit gets your permit. The binder runs the build — 367 pages of contracts, inspection ' +
  'forms, daily logs, and budget trackers covering every phase from footing to final, in the ' +
  'same print-and-go format.';

/**
 * Pick the states to link at the bottom of a kit page: the next three shipped
 * kits after this one, alphabetically, wrapping around the end of the list.
 * Every kit therefore links to three others and is linked from three others,
 * whether there are four kits or fifty — no editing as states ship, and no
 * page ends up orphaned.
 */
function siblingKits(slug: string) {
  const shipped = shippedKits();
  const here = shipped.findIndex((k) => k.slug === slug);
  if (here < 0) return [];
  return [1, 2, 3]
    .map((step) => shipped[(here + step) % shipped.length])
    .filter((k) => k && k.slug !== slug);
}

/**
 * The state permit kit product page. One layout for all 50 states: identity
 * and checkout come from STATE_KITS, prose comes from the KitContent object
 * the route hands in.
 */
export default function KitProductPage({ content }: { content: KitContent }) {
  const kit = kitBySlug(content.slug);
  if (!kit) {
    throw new Error(`KitProductPage: no STATE_KITS entry for slug "${content.slug}"`);
  }
  if (!kit.checkoutUrl) {
    throw new Error(
      `KitProductPage: ${kit.state} has no checkoutUrl in kits.ts — a kit page cannot ` +
        'ship without a payment link.'
    );
  }

  const { state, slug } = kit;
  const checkout = kit.checkoutUrl;
  const code = kit.code.toUpperCase();
  /** GA4 location prefix, matching the shipped kits: nck_, gak_, txk_, vak_. */
  const ev = `${kit.code.toLowerCase()}k`;
  const docCount = content.documents.length;
  const siblings = siblingKits(slug);
  const shippedCount = shippedKits().length;

  const productSchema = generateProductSchema({
    name: `${state} Owner-Builder Permit Kit`,
    description: content.productDescription,
    image: `${SITE_URL}${content.ogImage ?? '/binder/og-shop.jpg'}`,
    url: `${SITE_URL}/shop/${slug}`,
    price: KIT_PRICE,
    priceCurrency: 'USD',
    availability: 'InStock',
    brand: 'Build Your House',
    sku: slug,
  });
  const faqSchema = generateFAQSchema(content.faqs);

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
              <div className={`${styles.eyebrow} bp-eyebrow`}>{state} · Permit Kit</div>
              <h1 className={styles.heroTitle}>{state} Owner-Builder Permit Kit</h1>
              <p className={styles.heroSub}>{content.heroSub}</p>

              <div className={styles.dimstrip}>
                <div className={styles.dimcell}>
                  <span className={styles.k}>Pages</span>
                  <span className={styles.v}>{content.pageCount}</span>
                </div>
                <div className={styles.dimcell}>
                  <span className={styles.k}>Documents</span>
                  <span className={styles.v}>{dim(docCount)}</span>
                </div>
                <div className={styles.dimcell}>
                  <span className={styles.k}>Citations</span>
                  <span className={`${styles.v} ${styles.vText}`}>On-page</span>
                </div>
                <div className={styles.dimcell}>
                  <span className={styles.k}>Price</span>
                  <span className={`${styles.v} ${styles.vAccent}`}>${KIT_PRICE}</span>
                </div>
              </div>

              <div className={styles.heroCtas}>
                <TrackedLink
                  href={checkout}
                  eventName="begin_checkout"
                  eventParams={{
                    currency: 'USD',
                    value: KIT_PRICE,
                    item_name: slug,
                    location: 'hero',
                  }}
                  className={styles.btnPrimary}
                >
                  Get the kit — ${KIT_PRICE}
                </TrackedLink>
                <TrackedLink
                  href="#contents"
                  eventName="shop_cta_click"
                  eventParams={{ location: `${ev}_hero_see_inside`, item_name: slug }}
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
                  eventParams={{ location: `${ev}_hero_family`, context: slug }}
                  className={styles.familyLink}
                >
                  Job Site Binder family
                </TrackedLink>
              </p>
            </div>

            <div className={styles.stack}>
              <img
                src={content.heroSheets.back.src}
                alt={content.heroSheets.back.alt}
                width={700}
                height={906}
                className={`${styles.sheet} ${styles.sheetDark} ${styles.stackBack}`}
              />
              <img
                src={content.heroSheets.front.src}
                alt={content.heroSheets.front.alt}
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
              <h2 className={styles.secTitle}>
                {countWord(docCount)} documents, {content.pageCount} pages
              </h2>
            </div>
            <div className={styles.secMeta}>
              Print-ready PDFs
              <br />
              Letter size
            </div>
          </div>

          <div className={styles.index}>
            {content.documents.map((d) => (
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
              <div className={styles.secLabel}>Why it is worth ${KIT_PRICE}</div>
              <h2 className={styles.secTitle}>
                What the kit knows that the internet doesn&rsquo;t
              </h2>
            </div>
            <div className={styles.secMeta}>
              {countWord(content.highlights.length)} examples
              <br />
              All checkable
            </div>
          </div>

          <p className={styles.lead}>{content.highlightsLead}</p>

          <div className={styles.trust}>
            {content.highlights.map((h) => (
              <div key={h.label} className={styles.trustItem}>
                <Icon name={h.icon} size={26} className={styles.trustIco} />
                <div>
                  <p className={styles.trustLabel}>{h.label}</p>
                  <p className={styles.trustCopy}>{h.copy}</p>
                </div>
              </div>
            ))}
          </div>

          <p className={styles.trustSource}>{content.sourceNote}</p>
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
              <span className="bp-sheet-no">{code} Permit Kit</span>
              <span>Rev. {content.revision}</span>
            </div>

            <h3 className={styles.orderTitle}>The {state} Owner-Builder Permit Kit</h3>

            <p className={`${styles.inclLabel} bp-mono-label`}>What you get</p>
            <ul className={styles.incl}>
              {content.includes.map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>

            <div className={styles.priceRow}>
              <span className={styles.priceKey}>Price</span>
              <span className={styles.leader} aria-hidden="true" />
              <span className={styles.priceVal}>${KIT_PRICE}</span>
            </div>
            <div className={`${styles.orderDim} bp-dimline`}>One-time · Instant download</div>

            <TrackedLink
              href={checkout}
              eventName="begin_checkout"
              eventParams={{
                currency: 'USD',
                value: KIT_PRICE,
                item_name: slug,
                location: 'purchase_box',
              }}
              className={`${styles.btnPrimary} ${styles.orderCta}`}
            >
              Get the kit — ${KIT_PRICE}
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
                {content.verifyNote ??
                  'Statutes and code editions change. Confirm each rule with your county — the kit prints its sources so you can.'}
              </p>
              <p className={styles.spItem}>
                <span className={styles.spKey}>Payment</span>${KIT_PRICE} one-time. No
                subscription, no renewal.
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
            {content.faqs.map((f) => (
              <div key={f.question} className={styles.faqItem}>
                <h3 className={styles.faqQ}>{f.question}</h3>
                <p className={styles.faqA}>{f.answer}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ---------- RELATED ----------
          Generated from the registry: this state's free guide, then the next
          three kits in the line. Nothing here needs editing as states ship. */}
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
                href={`/permitting/state-guides/${kit.guideSlug}`}
                eventName="shop_cta_click"
                eventParams={{ location: `${ev}_related_guide`, context: slug }}
              >
                {state} owner-builder guide
              </TrackedLink>{' '}
              — the free overview this kit turns into working paper.
            </p>
            {siblings.map((s) => (
              <p key={s.slug} className={styles.spItem}>
                <span className={styles.spKey}>{s.state}</span>
                The{' '}
                <TrackedLink
                  href={`/shop/${s.slug}`}
                  eventName="shop_cta_click"
                  eventParams={{ location: `${ev}_related`, item_name: s.slug }}
                >
                  {s.code.toUpperCase()} Permit Kit
                </TrackedLink>
                , in the same {countWord(docCount).toLowerCase()}-document format.
              </p>
            ))}
          </div>

          <p className={styles.trustSource}>
            <TrackedLink
              href="/shop/permit-kits"
              eventName="shop_cta_click"
              eventParams={{ location: `${ev}_related_hub`, context: slug }}
            >
              All {shippedCount} state permit kits →
            </TrackedLink>
          </p>
        </div>
      </section>

      {/* ---------- CROSS-SELL ---------- */}
      <section className={styles.crossSell}>
        <div className={styles.wrap}>
          <BinderCTA context={slug} lead={content.binderLead ?? BINDER_LEAD} />
        </div>
      </section>
    </div>
  );
}
