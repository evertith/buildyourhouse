import type { Metadata } from 'next';
import s from '@/styles/CalcSheet.module.css';
import InsulationCalc from '@/components/calc/InsulationCalc';
import { CalcHero, CalcSection, AssumptionsTable, CalcFAQ, RelatedCalcs } from '@/components/calc/sections';
import BinderCTA from '@/components/BinderCTA';
import { generateFAQSchema, schemaToScriptTag } from '@/lib/schema';

export const metadata: Metadata = {
  alternates: { canonical: '/calculators/insulation' },
  title: 'Insulation Calculator — Batt Bags & Blown-In Coverage',
  description:
    'How much insulation do I need? Enter wall and attic square footage and get batt bag counts and blown-in coverage by R-value — with the bag-chart math shown.',
};

const FAQS = [
  {
    question: 'How many square feet does a bag of insulation cover?',
    answer:
      'Typical bag-chart coverage: R-13 batts run about 106 sq ft per bag, high-density R-15 about 68, R-19 about 87, and high-density R-21 about 68. Blown-in fiberglass covers roughly 40 sq ft per bag at R-38 and 31 sq ft at R-49. Coverage varies by brand because batt width, length, and count per bag all differ between manufacturers — the chart printed on the bag is the authority; these are rounded typical numbers for estimating.',
  },
  {
    question: 'What R-value do I need in my walls?',
    answer:
      '2×4 walls fit R-13 or R-15 batts; 2×6 walls fit R-19 or R-21. Which one your house needs comes from your climate zone and local energy code, not from a calculator — colder zones require more wall R-value, and some jurisdictions add continuous exterior foam on top. The insulation phase guide on this site has the climate-zone map; when in doubt, ask your building department what they enforce.',
  },
  {
    question: 'How many bags of blown-in insulation for 1,200 sq ft at R-38?',
    answer:
      'At roughly 40 sq ft of coverage per bag at R-38, a 1,200 sq ft attic takes 1,200 ÷ 40 = 30 bags. At $38–$52 per bag that is about $1,140–$1,560 in material, and at 30 bags the blower rental is usually free — most big boxes waive it with a purchase of around 10 bags or more.',
  },
  {
    question: 'Can I compress batts to fit a smaller cavity?',
    answer:
      'No. Fiberglass insulates with the air it traps; squash it and the R-value collapses — an R-19 batt compressed into a 2×4 cavity performs like R-13. Buy the batt made for your cavity depth, and cut around wires and boxes instead of stuffing the batt behind them.',
  },
  {
    question: 'Batts or blown-in for the attic?',
    answer:
      'For an open, accessible attic, blown-in usually wins: it fills irregular joist bays and odd gaps without cutting, goes in faster, and the blower rental is typically free with a ~10-bag purchase. Batts earn their keep at kneewalls, sloped ceilings, and tight-access areas where you cannot aim a hose, and on small jobs where renting and returning a machine is not worth the trip.',
  },
];

const faqSchema = generateFAQSchema(FAQS);

export default function InsulationPage() {
  return (
    <div className={s.calcPage}>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: schemaToScriptTag(faqSchema) }}
      />

      <CalcHero
        title="Insulation Calculator"
        sub="Batt bags for the walls, blown-in bags for the attic — figured from manufacturer bag charts, with the math shown, not hidden."
        cells={[
          { k: 'Sheet', v: 'TO-07' },
          { k: 'Returns', v: 'Bags' },
          { k: 'Basis', v: 'Bag charts' },
          { k: 'Deduction', v: '15% openings' },
        ]}
      />

      <div className={s.sheetWrap}>
        <InsulationCalc />
      </div>

      <div className={s.content}>
        <CalcSection label="Methodology" title="How this takeoff is figured" meta="SHEET TO-07">
          <div className={s.prose}>
            <p>
              <strong>Wall area.</strong> Perimeter × wall height × stories, minus 15% for windows
              and doors — the standard estimating deduction for a typical opening count. If you
              already know your net wall area, switch to the wall-area input and the calculator
              uses your number as-is.
            </p>
            <p>
              <strong>Wall batts.</strong> Wall area ÷ coverage per bag, plus a 5% cut allowance,
              rounded up to whole bags. Coverage per bag: R-13 ~106 sq ft, R-15 ~68, R-19 ~87,
              R-21 ~68 — rounded manufacturer bag-chart numbers, so check your brand&apos;s chart
              before ordering; batt width and count per bag vary.
            </p>
            <p>
              <strong>Blown-in attic.</strong> Attic area ÷ coverage per bag: blown-in fiberglass
              runs about 40 sq ft per bag at R-38 and 31 sq ft at R-49, rounded up to whole bags.
              The blower rental is usually free with a ~10-bag purchase, so plan the buy in one
              trip.
            </p>
            <p>
              <strong>Air-sealing first.</strong> Caulk and foam the top plates, wire holes, and
              flue penetrations before a single bag goes in — it is the highest-ROI hour on the
              job, and insulation will not stop the air leaks it merely hides.
            </p>
            <p>
              <strong>What&apos;s not here.</strong> Rim joists, basement walls, spray foam, and
              rigid exterior foam — those are sized from your plans and climate zone, not a
              coverage chart. R-value requirements come from local code; the{' '}
              <a href="/build-phases/insulation">insulation phase guide</a> has the climate-zone
              map.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Assumptions" title="Coverage, deductions, and prices" meta="ADJUST ABOVE">
          <AssumptionsTable
            rows={[
              { label: 'Batt coverage, R-13', value: '~106 sq ft/bag' },
              { label: 'Batt coverage, R-15', value: '~68 sq ft/bag' },
              { label: 'Batt coverage, R-19', value: '~87 sq ft/bag' },
              { label: 'Batt coverage, R-21', value: '~68 sq ft/bag' },
              { label: 'Blown-in coverage, R-38', value: '~40 sq ft/bag' },
              { label: 'Blown-in coverage, R-49', value: '~31 sq ft/bag' },
              { label: 'Wall openings deduction', value: '15%' },
              { label: 'Batt cut allowance', value: '5%' },
              { label: 'Batt bag prices', value: '$55–$95 by R-value' },
              { label: 'Blown-in bag price', value: '$38–$52' },
              { label: 'Prices', value: 'National range, Aug 2026' },
            ]}
          />
        </CalcSection>

        <CalcSection label="Questions" title="Owner-builders ask" meta="FAQ" noPrint>
          <CalcFAQ items={FAQS.map((f) => ({ question: f.question, answer: f.answer }))} />
        </CalcSection>

        <RelatedCalcs slug="insulation" />

        <div className={`${s.block} ${s.blockLast} no-print`}>
          <BinderCTA
            context="calc-insulation"
            lead="The binder's pre-drywall section includes the insulation inspection checklist — the walkthrough that happens before drywall hides the cavities: no compressed batts, no gaps, air-sealing done. 367 pages of job-site paperwork, organized the way a GC runs a build."
          />
        </div>
      </div>
    </div>
  );
}
