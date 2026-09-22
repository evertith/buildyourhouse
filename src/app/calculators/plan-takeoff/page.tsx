import type { Metadata } from 'next';
import s from '@/styles/CalcSheet.module.css';
import { CalcHero, CalcSection, CalcFAQ, RelatedCalcs } from '@/components/calc/sections';
import TrackedLink from '@/components/TrackedLink';
import { generateFAQSchema, schemaToScriptTag } from '@/lib/schema';
import { STUDTALLY_PRICE, studTallyUrl } from '@/lib/studtally';

export const metadata: Metadata = {
  alternates: { canonical: '/calculators/plan-takeoff' },
  title: 'Plan Set Takeoff — The Framing List From Your Drawings',
  description:
    'Upload a residential plan set and get a framing takeoff the lumber yard can key in, with every quantity traced back to the sheet it came from. StudTally, from the people behind this site. $79 per job, under an hour.',
};

const FAQS = [
  {
    question: 'What does StudTally give me?',
    answer:
      'A framing material list built from your plan set: the quantities the lumber yard needs to key in an order, with every number traced back to the drawing it came from. You review the measurements with the sheet beside them before the list is final, then download it as a PDF or a spreadsheet, or share a link to the takeoff.',
  },
  {
    question: 'How is this different from the free calculators on this site?',
    answer:
      'The free sheets estimate. The whole-house estimator works from square footage and a finish level; the framing lumber calculator works from wall lengths you type in. Both are honest planning numbers and neither reads your drawings. StudTally reads the plan set itself, which is why its output is an order list rather than an estimate.',
  },
  {
    question: 'What do I upload?',
    answer:
      'A residential plan set as a PDF, plus a few details about the build. StudTally measures the plan and reads the sheets that need reading. Where a detail needs your judgment, it asks, with the drawing in view.',
  },
  {
    question: 'How long does it take and what does it cost?',
    answer: `Under an hour, and $${STUDTALLY_PRICE} per job. There is no subscription; each plan set is one job.`,
  },
  {
    question: 'Who is it for?',
    answer:
      'An owner-builder heading to the lumber yard with a plan set in hand, anyone checking a framing bid against the drawings, and a framing sub who would rather review a traced list than count it by hand. If you do not have plans yet, start with the free estimator on this site and come back when you do.',
  },
  {
    question: 'Who built it?',
    answer:
      'The same people who build and maintain this site. StudTally is a separate product with its own account and payment, and this page exists because the fine print on every calculator here says to order after a takeoff from your actual plans. This is that takeoff.',
  },
];

const faqSchema = generateFAQSchema(FAQS);

export default function PlanTakeoffPage() {
  return (
    <div className={s.calcPage}>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: schemaToScriptTag(faqSchema) }}
      />

      <CalcHero
        flat
        eyebrow="Plan set takeoff"
        title="The framing list the yard can key in"
        sub="Upload a residential plan set. StudTally measures the plan, reads the sheets that need reading, and hands back a framing list with every number traced to the drawing it came from."
        cells={[
          { k: 'Sheet', v: 'PT-01' },
          { k: 'Input', v: 'Plan set PDF' },
          { k: 'Returns', v: 'Framing list' },
          { k: 'Price', v: `$${STUDTALLY_PRICE} per job` },
        ]}
      />

      <div className={s.content}>
        <CalcSection label="How it works" title="From the plan sheet to the lumber yard" meta="SHEET PT-01">
          <div className={s.prose}>
            <p>
              <strong>1. Upload your PDF.</strong> Add the plan set and a few details about
              the build.
            </p>
            <p>
              <strong>2. Review the measurements.</strong> Confirm the details that need your
              judgment, with the drawing beside them. Every quantity on the list points back to
              the sheet it came from, so a number you doubt is a number you can check.
            </p>
            <p>
              <strong>3. Take your list to the yard.</strong> Download a PDF or spreadsheet, or
              share a link to the takeoff. It is written to be keyed in, not interpreted.
            </p>
            <p>
              <TrackedLink
                href={studTallyUrl('plan-takeoff-page')}
                target="_blank"
                rel="noopener"
                className={s.planTakeoffLink}
                eventName="studtally_click"
                eventParams={{ calculator: 'plan-takeoff', location: 'page' }}
              >
                Upload a plan set at StudTally →
              </TrackedLink>
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Where it fits" title="Estimate here, order from there">
          <div className={s.prose}>
            <p>
              The calculators on this site are planning tools. The whole-house estimator turns
              square footage and a finish level into a budget range; the framing lumber sheet
              turns wall lengths into stud and plate counts. Both print their assumptions and
              both end with the same fine print: estimate only, order after a takeoff from your
              actual plans.
            </p>
            <p>
              StudTally is that takeoff. It reads the drawings instead of your inputs, so the
              list it returns is the one you hand across the counter. Use the free sheets to
              decide whether and what to build. Use StudTally once the plans exist and the
              lumber order is next.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Questions" title="Owner-builders ask" meta="FAQ" noPrint>
          <CalcFAQ items={FAQS.map((f) => ({ question: f.question, answer: f.answer }))} />
        </CalcSection>

        <RelatedCalcs slug="plan-takeoff" />

        <div className={`${s.block} ${s.blockLast} no-print`}>
          <div className={s.planTakeoff}>
            <p className={s.costDimLabel}>
              Ready when your plans are
              <span className={s.costDimNote}>StudTally</span>
            </p>
            <p className={s.planTakeoffText}>
              ${STUDTALLY_PRICE} per job, under an hour, every number traced to the sheet.
            </p>
            <TrackedLink
              href={studTallyUrl('plan-takeoff-page-footer')}
              target="_blank"
              rel="noopener"
              className={s.planTakeoffLink}
              eventName="studtally_click"
              eventParams={{ calculator: 'plan-takeoff', location: 'page-footer' }}
            >
              Upload a plan set at StudTally →
            </TrackedLink>
            <span className={s.planTakeoffMeta}>From the people behind this site</span>
          </div>
        </div>
      </div>
    </div>
  );
}
