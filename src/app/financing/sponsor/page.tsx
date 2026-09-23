import type { Metadata } from 'next';
import s from '@/styles/CalcSheet.module.css';
import f from '@/styles/Financing.module.css';
import { CalcHero, CalcSection, CalcFAQ } from '@/components/calc/sections';
import TrackedLink from '@/components/TrackedLink';
import { LENDERS } from '@/lib/financing/lenders';
import {
  NATIONAL_SPONSOR_PRICE,
  SPONSOR_CONTACT_EMAIL,
  SPONSOR_MIN_MONTHS,
  STATE_SPONSOR_FOUNDING_PRICE,
  STATE_SPONSOR_FOUNDING_SEATS,
  STATE_SPONSOR_PRICE,
} from '@/lib/financing/sponsors';

export const metadata: Metadata = {
  alternates: { canonical: '/financing/sponsor' },
  title: 'Sponsor the Owner-Builder Lender Directory',
  description:
    'Flat-fee, state-exclusive placement in the only lender directory built from lenders’ own published owner-builder acceptance, shown on that state’s owner-builder guide and the financing hub. Labeled Sponsored. No per-lead or per-closing fees.',
  robots: { index: true, follow: true },
};

/** Audience figures are stated as of a date and rounded down. Update with the date. */
const AUDIENCE_AS_OF = 'September 2026';
const STATS = [
  { k: 'Lenders listed', v: `${LENDERS.length}`, note: 'verified against their own sites' },
  { k: 'States covered', v: '50', note: 'the empty ones are named as empty' },
  { k: 'Readers', v: '2,000+ / mo', note: 'and roughly doubling each quarter' },
  { k: 'AI citations', v: '1,900 / wk', note: 'Copilot and partners, 22% share of authority' },
];

const FAQS = [
  {
    question: 'What does a sponsor actually get?',
    answer:
      'The top position, under a visible Sponsored label, in the lender module on that state’s owner-builder guide, which is the page people land on when they search whether they can build their own house there. The same placement sits at the top of the financing hub’s directory, labeled with your state. Your one-sentence pitch appears with the link, and the link carries rel="sponsored". One sponsor per state.',
  },
  {
    question: 'Why flat fee and not per lead?',
    answer:
      'Because this is advertising, and it stays advertising. We do not sell leads, we do not steer individual borrowers to a paying lender, and we do not take compensation tied to a closing. That keeps the placement on the right side of RESPA for both of us and keeps the directory honest for the reader. Your compliance team can review the arrangement; we will put it in writing.',
  },
  {
    question: 'Do we have to qualify?',
    answer:
      'Yes, the same way every lender in the editorial list qualified: your own website has to state that you accept owner-builders, in words a borrower can find. Lenders whose pages say self-builds are not accepted are not listed, sponsored or otherwise, and two well-known Farm Credit associations were removed on exactly that basis.',
  },
  {
    question: 'What do the numbers look like?',
    answer: `The site draws a little over two thousand readers a month as of ${AUDIENCE_AS_OF}, with clicks roughly doubling quarter over quarter, and it is cited about 1,900 times a week in Copilot answers. Financing intent is a fraction of that. We tell you the honest per-state figures before you commit, and you get a monthly count of impressions and clicks on your placement from our analytics.`,
  },
  {
    question: 'How does billing work?',
    answer: `Monthly, invoiced through Stripe, ${SPONSOR_MIN_MONTHS}-month minimum and month to month after that. The founding rate is locked for twelve months for the first ${STATE_SPONSOR_FOUNDING_SEATS} state sponsors. Cancel with thirty days’ notice.`,
  },
  {
    question: 'Who runs this?',
    answer:
      'A retired general contractor who built custom homes for fifteen years and now writes the state guides and the permit kits on this site. The directory exists because readers kept asking who would lend to them, and the answer turned out to be short and hard to find.',
  },
];

export default function SponsorPage() {
  const mailto = `mailto:${SPONSOR_CONTACT_EMAIL}?subject=${encodeURIComponent('Lender sponsorship — [state]')}`;
  return (
    <div className={s.calcPage}>
      <CalcHero
        flat
        eyebrow="For lenders"
        title="Sponsor the owner-builder lender directory"
        sub="Flat-fee, state-exclusive placement in the only directory built from what lenders publish about owner-builders, shown where those borrowers actually read."
        cells={[
          { k: 'Placement', v: 'Top of state module' },
          { k: 'Exclusivity', v: 'One per state' },
          { k: 'Label', v: 'Sponsored' },
          { k: 'Fee', v: 'Flat monthly' },
        ]}
      />

      <div className={s.content}>
        <CalcSection label="The audience" title="Who reads these pages" meta={`AS OF ${AUDIENCE_AS_OF.toUpperCase()}`}>
          <div className={s.prose}>
            <p>
              Owner-builders are the borrowers most lenders turn away and a few lenders build a
              business on. The people reading this site have searched whether they can legally
              build their own house in a specific state, and the state guide they land on is
              where the lender module sits. Nobody arrives here by accident.
            </p>
          </div>
          <div className={f.statGrid}>
            {STATS.map((x) => (
              <div key={x.k} className={f.stat}>
                <span className={f.statK}>{x.k}</span>
                <span className={f.statV}>{x.v}</span>
                <span className={f.statNote}>{x.note}</span>
              </div>
            ))}
          </div>
          <div className={s.prose}>
            <p>
              Those are site-wide figures, rounded down. Financing intent is a fraction of them,
              and we will show you the per-state page numbers before you decide. What you are
              buying is not volume. It is the top line on the one page an owner-builder in your state reads
              before they call anyone.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Rate card" title="Two placements, flat fees" meta="USD / MONTH">
          <div className={f.rateGrid}>
            <div className={f.rate}>
              <span className={f.rateName}>State sponsor</span>
              <span className={f.ratePrice}>${STATE_SPONSOR_PRICE}</span>
              <span className={f.rateNote}>
                Founding rate ${STATE_SPONSOR_FOUNDING_PRICE}, locked twelve months, first{' '}
                {STATE_SPONSOR_FOUNDING_SEATS} states
              </span>
              <ul className={f.rateList}>
                <li>Top of the lender module on that state’s owner-builder guide</li>
                <li>Top of the financing hub’s directory, labeled with your state</li>
                <li>Exclusive: one sponsor per state</li>
                <li>Your one-sentence pitch, approved by both sides</li>
                <li>Monthly impression and click report</li>
              </ul>
            </div>
            <div className={f.rate}>
              <span className={f.rateName}>National sponsor</span>
              <span className={f.ratePrice}>${NATIONAL_SPONSOR_PRICE}</span>
              <span className={f.rateNote}>For lenders licensed in many states</span>
              <ul className={f.rateList}>
                <li>The featured slot on the financing hub itself</li>
                <li>State-sponsor placement in every state you lend in that has no state sponsor</li>
                <li>Everything in the state tier</li>
              </ul>
            </div>
          </div>
          <div className={s.prose}>
            <p>
              {SPONSOR_MIN_MONTHS}-month minimum, then month to month. Invoiced through Stripe.
              No setup fee, no per-lead fee, no per-closing fee, ever.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="The rules" title="What keeps this honest">
          <div className={s.prose}>
            <p>
              <strong>Sponsored means sponsored.</strong> The placement carries a visible label
              and a rel="sponsored" link. The editorial list beneath it is not for sale and
              nobody in it has paid to be there.
            </p>
            <p>
              <strong>Same bar as the directory.</strong> Your site must say, in public, that you
              accept owner-builders. If it stops saying so, the placement pauses.
            </p>
            <p>
              <strong>Advertising, not referral.</strong> We publish a directory and sell
              placement in it. We do not hand you borrowers, route form submissions to you, or
              take a cent tied to a loan closing.
            </p>
            <p>
              <strong>Facts stay facts.</strong> Your pitch sentence describes what you
              advertise. We will not print a rate, a term, or a promise we cannot see on your
              own site.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Questions" title="Lenders ask" meta="FAQ" noPrint>
          <CalcFAQ items={FAQS} />
        </CalcSection>

        <div className={`${s.block} ${s.blockLast}`}>
          <div className={f.sponsored}>
            <span className={f.sponsoredTag}>Start here</span>
            <p className={f.lenderName}>Tell us the state and we reply with that state’s page numbers.</p>
            <p className={f.lenderNotes}>
              One email, no forms. Say which state or states you lend in and whether your site
              names owner-builders. We answer with the guide’s traffic for those states, the
              founding rate if seats remain, and a one-page agreement.
            </p>
            <p className={f.lenderName}>
              <TrackedLink
                eventName="sponsor_inquiry_click"
                eventParams={{ placement: 'sponsor-page' }}
                href={mailto}
              >
                {SPONSOR_CONTACT_EMAIL} →
              </TrackedLink>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
