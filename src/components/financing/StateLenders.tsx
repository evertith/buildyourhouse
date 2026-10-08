import s from '@/styles/Financing.module.css';
import TrackedLink from '@/components/TrackedLink';
import ImpressionSentinel from '@/components/ImpressionSentinel';
import { lendersForState, LENDERS_VERIFIED } from '@/lib/financing/lenders';
import { SPONSOR_PAGE, sponsorForState } from '@/lib/financing/sponsors';

interface Props {
  /** Two-letter state code. */
  code: string;
  /** Display name — "North Carolina". */
  state: string;
}

/**
 * Per-state lender module for the state guides: the lenders in the
 * editorial directory whose advertised footprint includes this state,
 * with the state's sponsor (if any) on top under a visible Sponsored
 * label. Editorial links stay nofollow; the sponsored link is
 * rel="sponsored". The house ad at the foot points lenders at the rate
 * card and is the only thing that renders when no sponsor exists.
 */
export default function StateLenders({ code, state }: Props) {
  const c = code.toUpperCase();
  const sponsor = sponsorForState(c);
  const lenders = lendersForState(c);

  return (
    <section className={`${s.stateLenders} no-print`} aria-labelledby={`lenders-${c}`}>
      <ImpressionSentinel placement="state-lenders" params={{ state: c, sponsored: Boolean(sponsor) }} />
      <div className={s.stateLendersHead}>
        <h2 id={`lenders-${c}`} className={s.stateLendersTitle}>
          Lenders advertising owner-builder loans in {state}
        </h2>
        <span className={s.stateLendersCount}>
          {lenders.length} listed · checked {LENDERS_VERIFIED}
        </span>
      </div>

      {sponsor && (
        <aside className={s.sponsored}>
          <span className={s.sponsoredTag}>Sponsored</span>
          <p className={s.lenderName}>
            <TrackedLink
              eventName="lender_click"
              eventParams={{ lender: sponsor.lenderId ?? sponsor.name, placement: 'guide-sponsored', state: c }}
              href={sponsor.url}
              target="_blank"
              rel="sponsored noopener"
            >
              {sponsor.name}
            </TrackedLink>
          </p>
          <p className={s.lenderNotes}>{sponsor.pitch}</p>
        </aside>
      )}

      {lenders.length === 0 ? (
        <p className={s.stateLendersEmpty}>
          We could not find a lender whose own website says it accepts owner-builders in{' '}
          {state}, as of {LENDERS_VERIFIED}. That is a finding, not an oversight: the lenders
          that do this work are community banks, credit unions and Farm Credit associations
          that write their own programs, and {state} does not have one that says so in
          public. Start with the community banks and the Farm Credit association nearest the
          land, and ask the one question that matters: do you write construction loans where
          the owner acts as general contractor?
        </p>
      ) : (
        lenders.map((l) => (
          <div key={l.id} className={s.lenderRow}>
            <div>
              <p className={s.lenderName}>
                <TrackedLink
                  eventName="lender_click"
                  eventParams={{ lender: l.id, placement: 'guide', state: c }}
                  href={l.url}
                  target="_blank"
                  rel="nofollow noopener"
                >
                  {l.name}
                </TrackedLink>
              </p>
              <span className={s.lenderKind}>{l.kind}</span>
              <span className={s.lenderStates}>{l.states}</span>
            </div>
            <p className={s.lenderNotes}>{l.notes}</p>
          </div>
        ))
      )}

      <p className={s.stateLendersFoot}>
        What each lender advertises on its own site, not an endorsement. Programs and
        footprints change; confirm your county before you plan around a listing.{' '}
        <a href="/financing#lender-directory">All 50 states and how the list is built.</a>
      </p>

      {!sponsor && (
        <p className={s.houseAd}>
          Lend to owner-builders in {state}?{' '}
          <TrackedLink
            eventName="sponsor_inquiry_click"
            eventParams={{ state: c, placement: 'guide' }}
            href={SPONSOR_PAGE}
          >
            Feature your program here →
          </TrackedLink>
        </p>
      )}
    </section>
  );
}
