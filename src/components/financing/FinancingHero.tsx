import TrackedLink from '@/components/TrackedLink';
import { LENDERS_VERIFIED } from '@/lib/financing/lenders';
import s from '@/styles/FinancingHero.module.css';

/**
 * Title band for /financing. The article shell already paints every MDX h1 as
 * a navy blueprint band (article.module.css); this replaces that default with
 * a full hero in the same language as /shop and /start-here — crop marks,
 * spec-sheet panel, mono sheet number — because /financing is a landing page
 * for the lender-match form, not just another guide.
 *
 * The two CTAs are the page's conversion pair in priority order: the form
 * first (#lender-match, owned by LenderMatchForm), then the directory.
 */

// Jump targets into the guide below the two conversion blocks. Ids live on the
// matching headings in page.mdx — the MDX pipeline has no slug plugin, so
// anchored sections carry hand-written ids.
const GUIDE_INDEX: { href: string; label: string }[] = [
  { href: '#loan-types', label: 'Loan types' },
  { href: '#requirements', label: 'Requirements' },
  { href: '#draws', label: 'Draw schedule' },
  { href: '#obstacles', label: 'Obstacles' },
  { href: '#alternatives', label: 'Alternatives' },
];

export default function FinancingHero() {
  return (
    <section className={`${s.hero} bp-band bp-grid`}>
      <span className={`${s.crop} ${s.tl}`} />
      <span className={`${s.crop} ${s.tr}`} />
      <span className={`${s.crop} ${s.bl}`} />
      <span className={`${s.crop} ${s.br}`} />

      <div className={s.inner}>
        <div className={s.grid}>
          <div>
            <div className={`${s.eyebrow} bp-eyebrow`}>FIN-01 · Financing</div>
            <h1 className={s.title}>
              Construction Loans for <em>Owner-Builders</em>
            </h1>
            <p className={s.lead}>
              The hard part usually isn&rsquo;t qualifying — it&rsquo;s finding a
              lender willing to write the loan without a licensed general contractor
              on the paperwork. This guide maps the five funding paths, the lenders
              who say yes, and what they will ask you for.
            </p>

            <div className={s.ctas}>
              <TrackedLink
                href="#lender-match"
                eventName="financing_cta_click"
                eventParams={{ location: 'hero_lender_match' }}
                className={s.btnPrimary}
              >
                Get your lender shortlist — free
              </TrackedLink>
              <TrackedLink
                href="#lender-directory"
                eventName="financing_cta_click"
                eventParams={{ location: 'hero_lender_directory' }}
                className={s.btnGhost}
              >
                See the lenders ↓
              </TrackedLink>
            </div>
            <p className={s.fine}>
              No obligation · A reply within a couple of business days
            </p>
          </div>

          <aside className={s.specsheet}>
            <div className={s.sheetNo}>
              <span>Sheet FIN-01</span>
              <span>Rev. 2026</span>
            </div>
            <div className={s.dimrow}>
              <span className={s.k}>Funding paths</span>
              <span className={s.v}>05</span>
            </div>
            <div className={s.dimrow}>
              <span className={s.k}>Directory checked</span>
              <span className={`${s.v} ${s.vText}`}>{LENDERS_VERIFIED}</span>
            </div>
            <div className={s.dimrow}>
              <span className={s.k}>Lender matching</span>
              <span className={`${s.v} ${s.vAccent}`}>Free</span>
            </div>
          </aside>
        </div>
      </div>

      {/* Sheet index along the bottom of the band: the guide is long and now
          sits under two conversion blocks, so the way in stays visible. */}
      <nav className={s.index} aria-label="Jump to the full guide">
        <span className={s.indexLabel}>In this guide</span>
        {GUIDE_INDEX.map((g) => (
          <a key={g.href} href={g.href} className={s.indexLink}>
            {g.label}
          </a>
        ))}
      </nav>
    </section>
  );
}
