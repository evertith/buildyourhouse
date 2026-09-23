import type { Metadata } from 'next';
import Link from 'next/link';
import s from '@/styles/CalcSheet.module.css';
import { CalcHero, CalcSection } from '@/components/calc/sections';
import EmailCapture from '@/components/EmailCapture';
import BinderCTA from '@/components/BinderCTA';

/**
 * The hiring-a-builder door. Every owner-builder state guide forks here from
 * its first screen for the reader who has just decided to hire instead.
 * Kept out of the index until the state-by-state hiring guides exist; its
 * job today is to be honest, useful for ten minutes, and to measure demand
 * (fork clicks arrive with ?state=XX; the capture carries the source path).
 */
export const metadata: Metadata = {
  alternates: { canonical: '/hiring-a-builder' },
  title: 'Hiring a Builder for Your Custom Home',
  description:
    'What changes when you hire a general contractor instead of being one: the license lookup, the contract, lien law, and the draw schedule — by a retired GC. State-by-state guides in progress.',
  robots: { index: false, follow: true },
};

export default function HiringABuilderPage() {
  return (
    <div className={s.calcPage}>
      <CalcHero
        flat
        eyebrow="Hiring a builder"
        title="Building a custom home with a contractor"
        sub="The owner-builder guides on this site cover the permit and code side of a build. This page is the door for the reader who has decided to hire the building out — what changes, what to check first, and where the state-by-state guides for that decision stand."
        cells={[
          { k: 'Written by', v: 'A retired GC' },
          { k: 'Scope', v: 'You as the client' },
          { k: 'State guides', v: 'In progress' },
          { k: 'Cost', v: 'Free' },
        ]}
      />

      <div className={s.content}>
        <CalcSection label="What changes" title="You stop being the contractor and start being the client">
          <div className={s.prose}>
            <p>
              Everything on the owner-builder side of this site assumes you hold the permit and
              carry the liability. Hire a general contractor and four things move onto their side
              of the table, and four new ones land on yours.
            </p>
            <p>
              <strong>Their license is now your protection, so verify it yourself.</strong> Every
              state that licenses residential contractors runs a public lookup. Check the name on
              the contract against it, check that the license is active and in the right
              classification for a house of your size, and check the complaint history. Do it
              before you sign, not after the first draw.
            </p>
            <p>
              <strong>The contract is the whole relationship.</strong> Fixed price or cost-plus,
              what an allowance is and what happens when you exceed one, how a change order is
              priced and approved, who owns delays, and what the warranty actually covers. A
              retired GC will tell you that most disputes were written into the contract on day
              one by omission.
            </p>
            <p>
              <strong>Lien law runs the other way now.</strong> As an owner-builder you protect
              yourself from your subs. As a client you protect yourself from your builder's subs
              and suppliers, who can lien your house for work your builder was paid for and did
              not pass along. Lien releases at every draw are the paper that stops that, and the
              rule for them is set by your state.
            </p>
            <p>
              <strong>The draw schedule is the only leverage you keep.</strong> Money should follow
              inspected, completed work, never the calendar. The lender's inspector is on your
              side here; so is the permit card, which records what passed and when.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Where this is going" title="State-by-state guides for hiring, built the same way">
          <div className={s.prose}>
            <p>
              The owner-builder guides earned their keep by citing the statute on the page instead
              of summarizing someone else's summary. The hiring guides will do the same for the
              client's side: what your builder's contract can and cannot do in your state, the
              lien and draw rules that protect you, warranty and licensing law, and what happens
              when a builder walks. They are being written for the states with the most readers
              first.
            </p>
            <p>
              Until yours exists, the{' '}
              <Link href="/permitting/state-guides">owner-builder guide for your state</Link> is
              still the best plain-English account of the code, permit, and inspection sequence
              your builder will be working through, and the{' '}
              <Link href="/financing">financing page</Link> covers construction loans, which are
              the same product whether or not you swing the hammer.
            </p>
          </div>
        </CalcSection>

        <div className={s.block}>
          <EmailCapture title="Tell us your state and we will write yours sooner" />
        </div>

        <div className={`${s.block} ${s.blockLast}`}>
          <BinderCTA
            context="hiring-a-builder"
            lead="Most of the Job Site Binder is paperwork a client needs as much as an owner-builder does: the draw tracker, change-order log, inspection record, and selections and allowance sheets. It is the file you bring to every meeting with your builder."
          />
        </div>
      </div>
    </div>
  );
}
