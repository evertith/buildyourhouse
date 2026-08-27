import Link from 'next/link';
import type { Metadata } from 'next';
import EmailCapture from '@/components/EmailCapture';
import BinderCTA from '@/components/BinderCTA';
import StatePlate from '@/components/shop/StatePlate';
import { STATE_KITS, shippedKits, comingKits } from '@/lib/kits';
import { KIT_PRICE, dim } from '@/lib/kit-content';
import styles from './permit-kits.module.css';

export const metadata: Metadata = {
  alternates: { canonical: '/shop/permit-kits' },
  title: 'State Permit Kits for Owner-Builders — One Kit Per State',
  description:
    'State-specific owner-builder permit kits: the exemption walkthrough, permit application checklist, inspection sequence, and where-to-file directory — statute citations printed on the page. $34 per state.',
};

/**
 * The six slots every kit fills, whatever the state. Slot .1 is titled for
 * the state on the product page — Texas has no contractor license to be
 * exempt from, so its version covers what stands in for one.
 */
const FORMAT: { slot: string; title: string; copy: string }[] = [
  {
    slot: '.0',
    title: 'Cover & How to Use',
    copy: 'What is in the kit, what order to work through it, and which documents you file versus which you keep on the truck.',
  },
  {
    slot: '.1',
    title: 'Owner-Builder Exemption Walkthrough',
    copy: 'What you must own, what you must occupy, and how long you cannot sell — with the affidavit you sign before the permit issues. In states with no contractor license to be exempt from, this document covers the trade licensing and code rules that bind you instead.',
  },
  {
    slot: '.2',
    title: 'Permit Application Checklist',
    copy: 'Everything the permit office wants in the packet, in the order they ask for it: site plan, plans and specs, septic or sewer proof, and the state-specific filings. Work through it and the application is complete.',
  },
  {
    slot: '.3',
    title: 'Inspection Sequence',
    copy: 'Every inspection the state calls for, in the order it is called, with what the inspector looks at and what has to be finished before you can schedule it. Footing through final, trades included.',
  },
  {
    slot: '.4',
    title: 'Where-to-File Directory',
    copy: 'Which office handles which piece — building, electrical, septic, driveway, and the filings that never go through the building department at all.',
  },
  {
    slot: '.5',
    title: 'Forms & Documents Index',
    copy: 'Every form the kit references, with its official name and the office that issues it, so you can pull a current copy yourself.',
  },
];

export default function PermitKitsPage() {
  const shipped = shippedKits();
  const pending = comingKits().length;
  const total = STATE_KITS.length;

  return (
    <div className={styles.page}>
      {/* ---------- HERO ---------- */}
      <section className={`${styles.hero} bp-band bp-grid`}>
        <span className={`${styles.crop} ${styles.tl}`} />
        <span className={`${styles.crop} ${styles.tr}`} />
        <span className={`${styles.crop} ${styles.bl}`} />
        <span className={`${styles.crop} ${styles.br}`} />
        <div className={styles.heroInner}>
          <div className={styles.heroBody}>
            <p className={`${styles.eyebrow} bp-eyebrow`}>
              State permit kits · ${KIT_PRICE} each
            </p>
            <h1 className={styles.heroTitle}>
              Your State&apos;s Permitting Rules, as a Working Kit
            </h1>
            <p className={styles.heroCopy}>
              Permitting is a state problem. Every state writes its own owner-builder exemption,
              its own application packet, and its own inspection order — so there is one kit per
              state, built against that state&apos;s statutes and agencies, with the citations
              printed on the page where a permit clerk can check your work.
            </p>

            <div className={styles.dimstrip}>
              <div className={styles.dimcell}>
                <span className={styles.k}>Issued</span>
                <span className={styles.v}>
                  {dim(shipped.length)}
                  <span className={styles.vOf}>/{total}</span>
                </span>
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
                <span className={`${styles.v} ${styles.vAccent}`}>${KIT_PRICE}</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ---------- COVERAGE PLATE ---------- */}
      <section id="coverage" className={`${styles.block} ${styles.anchor}`}>
        <div className={styles.wrap}>
          <div className={styles.secHead}>
            <div>
              <div className={styles.secLabel}>Coverage</div>
              <h2 className={styles.secTitle}>Fifty states, one kit each</h2>
            </div>
            <div className={styles.secMeta}>
              Alphabetical
              <br />
              Find your state
            </div>
          </div>

          <StatePlate coming="anchor" comingHref="#request" />

          <div className={styles.legend}>
            <span className={styles.legendItem}>
              <span className={`${styles.swatch} ${styles.swatchOn}`} aria-hidden="true" />
              Built and ready to download
            </span>
            {pending > 0 && (
              <span className={styles.legendItem}>
                <span className={styles.swatch} aria-hidden="true" />
                In production — click to ask for yours next
              </span>
            )}
          </div>

          <p className={styles.plateNote}>
            {pending > 0
              ? 'Kits are built in phases of four, and which states come next is decided by what readers ask for. '
              : 'Every state is covered, and each kit is revised when its statutes or code editions change. '}
            Every state also has a free{' '}
            <Link href="/permitting/state-guides">owner-builder permitting guide</Link>.
          </p>
        </div>
      </section>

      {/* ---------- ISSUE INDEX ----------
          The drawing-set index for the line: one ruled row per issued kit,
          alphabetical, growing from four rows to fifty as states ship. */}
      <section id="kits" className={`${styles.block} ${styles.blockTight} ${styles.anchor}`}>
        <div className={styles.wrap}>
          <div className={styles.secHead}>
            <div>
              <div className={styles.secLabel}>Available now</div>
              <h2 className={styles.secTitle}>Buy your state&apos;s kit</h2>
            </div>
            <div className={styles.secMeta}>
              {shipped.length} of {total} states
              <br />
              Instant download
            </div>
          </div>

          <div className={styles.index}>
            {shipped.map((k) => (
              <Link key={k.slug} href={`/shop/${k.slug}`} className={styles.kitRow}>
                <span className={styles.kitNo}>
                  PK-{k.code.toUpperCase()}
                  <span className={styles.kitNoSub}>Issued</span>
                </span>
                <span className={styles.kitMain}>
                  <h3 className={styles.kitState}>{k.state}</h3>
                  <span className={styles.kitHook}>{k.hook}</span>
                </span>
                <span className={styles.kitBuy}>
                  ${KIT_PRICE}
                  <span className={styles.kitGo}>See the kit →</span>
                </span>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* ---------- THE FORMAT ---------- */}
      <section className={styles.block}>
        <div className={styles.wrap}>
          <div className={styles.secHead}>
            <div>
              <div className={styles.secLabel}>The format</div>
              <h2 className={styles.secTitle}>Every kit is the same six documents</h2>
            </div>
            <div className={styles.secMeta}>
              Print-ready PDFs
              <br />
              Letter size
            </div>
          </div>

          <p className={styles.lead}>
            A kit is not a rewritten guide — it is the paperwork. The same six documents every
            time, rebuilt against one state&apos;s statutes and agencies, so a kit for one state
            reads exactly like a kit for any other.
          </p>

          <div className={styles.index}>
            {FORMAT.map((d) => (
              <div key={d.slot} className={styles.docRow}>
                <span className={styles.docNo}>
                  <span className={styles.docProto}>XX</span>
                  {d.slot}
                </span>
                <div>
                  <h3 className={styles.docTitle}>{d.title}</h3>
                  <p className={styles.docCopy}>{d.copy}</p>
                </div>
              </div>
            ))}
          </div>

          <p className={styles.formatNote}>
            About 30 pages per kit · Print-ready PDF, letter size · Citations printed beside the
            rules
          </p>
        </div>
      </section>

      {/* ---------- REQUEST A STATE ---------- */}
      <section id="request" className={`${styles.block} ${styles.blockTight} ${styles.anchor}`}>
        <div className={styles.wrap}>
          <div className={styles.secHead}>
            <div>
              <div className={styles.secLabel}>
                {pending > 0 ? 'Request a state' : 'Stay current'}
              </div>
              <h2 className={styles.secTitle}>
                {pending > 0 ? 'Not your state yet?' : 'All fifty states are out'}
              </h2>
            </div>
            <div className={styles.secMeta}>
              {pending > 0 ? (
                <>
                  {pending} in production
                  <br />
                  Four ship at a time
                </>
              ) : (
                <>
                  {total} of {total}
                  <br />
                  Revised as codes change
                </>
              )}
            </div>
          </div>

          <div className={styles.capture}>
            <EmailCapture
              title={pending > 0 ? 'Building in another state?' : 'Building this year?'}
              description={
                pending > 0
                  ? 'Tell us where — the states we build kits for next come straight from these requests. You’ll get the owner-builder newsletter, and a note the day your state’s kit ships.'
                  : 'Every state has a kit now, and each one gets revised when its statutes or code editions change. Join the owner-builder newsletter and we’ll tell you when yours is updated.'
              }
              buttonText={pending > 0 ? 'Request my state' : 'Keep me posted'}
              placeholderText="you@example.com"
            />
          </div>
        </div>
      </section>

      {/* ---------- CROSS-SELL ---------- */}
      <section className={styles.crossSell}>
        <div className={styles.wrap}>
          <BinderCTA
            context="permit-kits"
            lead="The kit gets your permit. The binder runs the build — 367 pages of contracts, inspection forms, daily logs, and budget trackers covering every phase from footing to final, in the same print-and-go format."
          />
        </div>
      </section>
    </div>
  );
}
