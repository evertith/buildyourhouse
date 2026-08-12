import s from '@/styles/Financing.module.css';
import TrackedLink from '@/components/TrackedLink';
import { FEATURED_LENDER, LENDERS, LENDERS_VERIFIED } from '@/lib/financing/lenders';

/**
 * Editorial list of lenders that publicly advertise owner-builder programs.
 * Outbound clicks fire `lender_click` — the number that proves traffic
 * value in lender outreach. Links are nofollow (commercial outbound,
 * unpaid); a paid placement renders via FeaturedLenderSlot instead.
 */
export default function LenderDirectory() {
  return (
    <div className={s.directory}>
      <div className={s.dirHead}>
        <p className={s.dirTitle}>Lenders advertising owner-builder programs</p>
        <p className={s.dirVerified}>Checked {LENDERS_VERIFIED}</p>
      </div>
      {LENDERS.map((l) => (
        <div key={l.id} className={s.lenderRow}>
          <div>
            <p className={s.lenderName}>
              <TrackedLink
                eventName="lender_click"
                eventParams={{ lender: l.id }}
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
      ))}
      <p className={s.dirFoot}>
        What each lender advertises, not an endorsement — programs, states, and terms
        change, so verify directly before applying. No lender pays us to appear here;
        if a sponsored placement ever exists, it will be labeled as such.
      </p>
    </div>
  );
}

/** Renders only when a sponsorship deal is configured in lenders.ts. */
export function FeaturedLenderSlot() {
  if (!FEATURED_LENDER) return null;
  const f = FEATURED_LENDER;
  return (
    <aside className={s.sponsored}>
      <span className={s.sponsoredTag}>Sponsored</span>
      <p className={s.lenderName}>
        <TrackedLink
          eventName="lender_click"
          eventParams={{ lender: f.name, placement: 'sponsored' }}
          href={f.url}
          target="_blank"
          rel="sponsored noopener"
        >
          {f.name}
        </TrackedLink>
      </p>
      <span className={s.lenderStates}>{f.states}</span>
      <p className={s.lenderNotes}>{f.pitch}</p>
    </aside>
  );
}
