import Link from 'next/link';
import type { Metadata } from 'next';
import EmailCapture from '@/components/EmailCapture';
import styles from './permit-kits.module.css';

export const metadata: Metadata = {
  alternates: { canonical: '/shop/permit-kits' },
  title: 'State Permit Kits for Owner-Builders — NC, GA, TX & VA',
  description:
    'State-specific owner-builder permit kits: the exemption walkthrough, permit application checklist, inspection sequence, and where-to-file directory — statute citations printed on the page. $34 per state.',
};

const KITS = [
  {
    href: '/shop/nc-permit-kit',
    code: 'NC',
    state: 'North Carolina',
    hook: 'The owner exemption affidavit, the $40K lien-agent threshold, septic gating the permit, and the personally-present inspection rule.',
  },
  {
    href: '/shop/ga-permit-kit',
    code: 'GA',
    state: 'Georgia',
    hook: 'The one-sale-per-24-months exemption trap, mandatory codes even in no-permit counties, and the two required performance tests.',
  },
  {
    href: '/shop/tx-permit-kit',
    code: 'TX',
    state: 'Texas',
    hook: 'No state license or permit — and the traps that replace them: trade licensing, TCEQ septic, the energy code that applies anyway, coastal windstorm.',
  },
  {
    href: '/shop/va-permit-kit',
    code: 'VA',
    state: 'Virginia',
    hook: 'The § 54.1-1101 exemption, the lien agent that protects you, VDH septic shot clocks, and the VDOT driveway permit almost nobody expects.',
  },
];

export default function PermitKitsPage() {
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
            <p className={`${styles.eyebrow} bp-eyebrow`}>State permit kits · $34 each</p>
            <h1 className={styles.heroTitle}>
              Your State&apos;s Permitting Rules, as a Working Kit
            </h1>
            <p className={styles.heroCopy}>
              Each kit is the same six documents, built for one state and verified against
              that state&apos;s statutes and agencies: the owner-builder exemption walkthrough,
              the permit application checklist, the inspection sequence, a where-to-file
              directory, and a forms index — with the citations printed on the page, so a
              permit clerk can check your work.
            </p>

            <div className={styles.dimstrip}>
              <div className={styles.dimcell}>
                <span className={styles.k}>States</span>
                <span className={styles.v}>04</span>
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
                <span className={`${styles.v} ${styles.vAccent}`}>$34</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ---------- KIT INDEX ---------- */}
      <section className={styles.block}>
        <div className={styles.wrap}>
          <div className={styles.secHead}>
            <div>
              <div className={styles.secLabel}>Available now</div>
              <h2 className={styles.secTitle}>One kit per state</h2>
            </div>
            <div className={styles.secMeta}>
              Instant download
              <br />
              Print-ready
            </div>
          </div>

          <div className={styles.index}>
            {KITS.map((k) => (
              <Link key={k.href} href={k.href} className={styles.kitRow}>
                <div className={styles.kitCode}>
                  {k.code}
                  <span className={styles.kitCodeSub}>Permit kit</span>
                </div>
                <div className={styles.kitMain}>
                  <h3 className={styles.kitState}>{k.state}</h3>
                  <p className={styles.kitHook}>{k.hook}</p>
                  <span className={styles.kitGo}>
                    See the {k.state} kit <span aria-hidden="true">→</span>
                  </span>
                </div>
                <div className={styles.kitPrice}>
                  $34
                  <span className={styles.kitPriceNote}>Instant download</span>
                </div>
              </Link>
            ))}

            <div className={`${styles.kitRow} ${styles.kitRowQuiet}`}>
              <div className={styles.kitCode}>
                ··
                <span className={styles.kitCodeSub}>In progress</span>
              </div>
              <div className={styles.kitMain}>
                <h3 className={styles.kitState}>More states coming</h3>
                <p className={styles.kitHook}>
                  Which state gets built next comes straight from reader requests — tell us
                  where you&apos;re building and we&apos;ll put it in the queue.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ---------- REQUEST A STATE ---------- */}
      <section className={`${styles.block} ${styles.blockTight}`}>
        <div className={styles.wrap}>
          <div className={styles.capture}>
            <EmailCapture
              title="Building in another state?"
              description="Tell us where — the states we build kits for next come straight from these requests. You'll get the owner-builder newsletter, and a note when your state's kit ships."
              buttonText="Request my state"
              placeholderText="you@example.com"
            />
          </div>
        </div>
      </section>
    </div>
  );
}
