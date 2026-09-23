import s from '@/styles/Financing.module.css';
import ImpressionSentinel from '@/components/ImpressionSentinel';
import TrackedLink from '@/components/TrackedLink';
import { lendersForState } from '@/lib/financing/lenders';
import { sponsorForState } from '@/lib/financing/sponsors';

interface Props {
  code: string;
  state: string;
}

/**
 * The first-screen line for lenders: one sentence under the at-a-glance
 * table, because that is as far as most readers go. Editorial: a count and
 * an anchor to the full module. Sponsored: the sponsor's name and sentence,
 * labeled, rel="sponsored", with its own impression event — the number the
 * rate card promises.
 */
export default function StateLendersLine({ code, state }: Props) {
  const c = code.toUpperCase();
  const sponsor = sponsorForState(c);
  const n = lendersForState(c).length;

  if (sponsor) {
    return (
      <p className={`${s.lenderLine} ${s.lenderLineSponsored} no-print`}>
        <ImpressionSentinel placement="lender-line-sponsored" params={{ state: c, lender: sponsor.lenderId ?? sponsor.name }} />
        <span className={s.sponsoredTag}>Sponsored</span>{' '}
        <TrackedLink
          href={sponsor.url}
          target="_blank"
          rel="sponsored noopener"
          eventName="lender_click"
          eventParams={{ lender: sponsor.lenderId ?? sponsor.name, placement: 'guide-line-sponsored', state: c }}
          className={s.lenderLineName}
        >
          {sponsor.name}
        </TrackedLink>{' '}
        <span className={s.lenderLinePitch}>{sponsor.pitch}</span>{' '}
        <a href={`#lenders-${c}`} className={s.lenderLineMore}>
          {n} lender{n === 1 ? '' : 's'} advertise owner-builder loans in {state} ↓
        </a>
      </p>
    );
  }

  return (
    <p className={`${s.lenderLine} no-print`}>
      <ImpressionSentinel placement="lender-line" params={{ state: c }} />
      <span className={s.lenderLineK}>Financing</span>{' '}
      <a href={`#lenders-${c}`} className={s.lenderLineMore}>
        {n} lender{n === 1 ? '' : 's'} advertise owner-builder construction loans in {state} ↓
      </a>
    </p>
  );
}
