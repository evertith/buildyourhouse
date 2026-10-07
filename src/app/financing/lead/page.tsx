import type { Metadata } from 'next';
import s from '@/styles/CalcSheet.module.css';
import f from '@/styles/Financing.module.css';
import { CalcHero, CalcSection, CalcFAQ } from '@/components/calc/sections';
import TrackedLink from '@/components/TrackedLink';
import LeadOffer from '@/components/financing/LeadOffer';
import {
  LEAD_PRICE,
  STATE_SPONSOR_PRICE,
  SPONSOR_PAGE,
  SPONSOR_CONTACT_EMAIL,
} from '@/lib/financing/sponsors';

/**
 * Lender-facing: buy one consented borrower introduction. Not indexed and not
 * in the sitemap — Seth sends the link, with the borrower's anonymized details
 * in the query string (see LeadOffer). The terms on this page are the product:
 * flat fee, one lender, consent before delivery, nothing tied to a closing.
 */
export const metadata: Metadata = {
  title: 'Borrower introduction for lenders | Build Your House',
  description:
    'A flat-fee, consented introduction to one owner-builder borrower who asked Build Your House which lenders to call.',
  robots: { index: false, follow: false },
};

const FAQS = [
  {
    question: 'Why is the fee flat?',
    answer:
      'Because the fee is for the introduction, not for a loan. It is the same whether the borrower applies, is declined, or closes, and no part of it is tied to loan amount, rate, or terms. We never take per-closing compensation from anyone. That keeps the arrangement on the right side of RESPA for both of us, and we will put it in writing for your compliance team.',
  },
  {
    question: 'Can we see more before paying?',
    answer:
      'You see what is on this page: state, timeline, self-reported credit band, land status, and budget band, exactly as the borrower entered them. Name, email, phone, and the borrower’s own description of the project come after payment and after the borrower’s written yes.',
  },
  {
    question: 'What if the borrower says no?',
    answer:
      'Full refund within one business day. The same if they have gone quiet by the time we ask. You only pay for an introduction that actually happens.',
  },
  {
    question: 'Did you tell the borrower to use us?',
    answer:
      'No. They got the reply the form promises everyone: the lenders in our directory that fit their state and situation. Your payment does not change that reply, and we do not tell any borrower which lender to choose. We tell them who you are and what your own site says about owner-builder loans.',
  },
  {
    question: 'Is this exclusive?',
    answer:
      'The introduction is sold to one lender and never resold. The borrower is a free person who may also call lenders from our directory or anywhere else; we make no promise about that and would not want to.',
  },
  {
    question: 'We lend in this state every month. Is there a better deal?',
    answer: `Yes. A state sponsorship is $${STATE_SPONSOR_PRICE} a month, flat, for the top of the lender module on that state’s owner-builder guide, which is the page these borrowers read before they fill in the form. Details on the sponsor page.`,
  },
];

export default function LeadPage() {
  const mailto = `mailto:${SPONSOR_CONTACT_EMAIL}?subject=${encodeURIComponent('Borrower introduction')}`;
  return (
    <div className={s.calcPage}>
      <CalcHero
        flat
        eyebrow="For lenders"
        title="One owner-builder borrower, introduced to you"
        sub="They asked us which lenders to call. You pay a flat fee, we confirm they want the introduction, and their details land in your inbox within one business day."
        cells={[
          { k: 'Fee', v: `$${LEAD_PRICE} flat` },
          { k: 'Lenders', v: 'One' },
          { k: 'Consent', v: 'In writing' },
          { k: 'Delivery', v: '1 business day' },
        ]}
      />

      <div className={s.content}>
        <CalcSection label="The borrower" title="What they told us" meta="AS ENTERED ON THE FORM">
          <div className={s.prose}>
            <p>
              Every field below is the borrower’s own answer on our lender-match form, which
              sits on the owner-builder financing hub and on every state guide. Nobody fills it in
              by accident: the form asks for timeline, credit band, land status, and budget, and
              the reply it promises is a short list of lenders that fit.
            </p>
          </div>
          <LeadOffer />
        </CalcSection>

        <CalcSection label="What you get" title="After the borrower says yes">
          <div className={s.prose}>
            <p>
              <strong>Name, email, and phone</strong> if they gave one, plus everything above, plus
              the borrower’s own description of the project from the form, and the date they agreed
              to the introduction. It arrives by reply to your receipt email, from Seth, within one
              business day of their yes.
            </p>
            <p>
              <strong>What you do not get:</strong> any promise that they apply or close, and any
              hold on the borrower. They may call other lenders, including the ones we named in our
              reply to them.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="The terms" title="What keeps this honest">
          <div className={s.prose}>
            <p>
              <strong>Flat fee, not contingent.</strong> ${LEAD_PRICE} for the introduction. The same
              whether or not a loan closes, and nothing tied to loan amount, rate, or terms. We never
              take per-closing compensation.
            </p>
            <p>
              <strong>Consent before details.</strong> Nothing that identifies the borrower leaves
              this site until they agree, in writing, to be introduced to you by name. If they
              decline, you are refunded in full within one business day.
            </p>
            <p>
              <strong>Sold once.</strong> One lender gets this introduction. We do not resell it and
              we do not auction it.
            </p>
            <p>
              <strong>No steering.</strong> The borrower received the reply everyone receives: the
              directory lenders that fit their state and situation. Your payment changes nothing in
              that reply, and we do not tell borrowers which lender to choose.
            </p>
            <p>
              <strong>Dead contact, full refund.</strong> If the email bounces or the number is
              wrong, say so within seven days.
            </p>
            <p>
              <strong>Who we are.</strong> Build Your House is a publisher. We are not a mortgage
              broker or a lender, and we do not originate, arrange, or negotiate loans. Your outreach
              to the borrower is yours; our consent covers a person reaching out, so follow your own
              rules for automated calls or texts.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Questions" title="Lenders ask" meta="FAQ" noPrint>
          <CalcFAQ items={FAQS} />
        </CalcSection>

        <div className={`${s.block} ${s.blockLast}`}>
          <div className={f.sponsored}>
            <span className={f.sponsoredTag}>Lend here often?</span>
            <p className={f.lenderName}>
              State sponsorship is ${STATE_SPONSOR_PRICE} a month, flat, on the page these borrowers read first.
            </p>
            <p className={f.lenderNotes}>
              Top of the lender module on that state’s owner-builder guide and the financing hub,
              under a visible Sponsored label, one sponsor per state. No per-lead fee, no
              per-closing fee, ever.
            </p>
            <p className={f.lenderName}>
              <TrackedLink
                eventName="sponsor_inquiry_click"
                eventParams={{ placement: 'lead-page' }}
                href={SPONSOR_PAGE}
              >
                The sponsor rate card →
              </TrackedLink>
            </p>
            <p className={f.lenderNotes}>
              Questions about this introduction:{' '}
              <a href={mailto}>{SPONSOR_CONTACT_EMAIL}</a>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
