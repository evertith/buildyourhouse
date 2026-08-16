import type { Metadata } from 'next';
import s from '@/styles/CalcSheet.module.css';
import BudgetTrackerCalc from '@/components/calc/BudgetTrackerCalc';
import { CalcHero, CalcSection, AssumptionsTable, CalcFAQ, RelatedCalcs } from '@/components/calc/sections';
import BinderCTA from '@/components/BinderCTA';
import { generateFAQSchema, schemaToScriptTag } from '@/lib/schema';

export const metadata: Metadata = {
  alternates: { canonical: '/calculators/budget-tracker' },
  title: 'Free Construction Budget Tracker — Budgeted vs. Actual Costs',
  description:
    'Track your owner-builder budget in real time. Compare budgeted vs. actual costs by phase, spot overruns early, and stay on track.',
};

const FAQS = [
  {
    question: 'How much contingency should an owner-builder budget?',
    answer:
      'Ten to twenty percent of the planned total, and 15% is the usual starting point on this sheet. Below 10% you are betting that nothing goes wrong on a project with hundreds of ways to go wrong. Above 20% and you are probably padding a budget you do not trust — tighten the estimate instead, because a fat contingency tends to get spent.',
  },
  {
    question: 'What is budget variance, and when should I worry?',
    answer:
      'Variance is planned minus actual for each phase: positive means the phase came in under, negative means it ran over. This sheet counts a phase as on track while it is within 5% of plan. Worry when the overruns cluster early — a 10% overrun on foundation, framing, and rough-ins puts you 30% over before you have bought a single cabinet.',
  },
  {
    question: 'When have I used too much contingency?',
    answer:
      'Compare the reserve you have burned to the share of the project still ahead of you. If you have spent more than half the contingency by the halfway mark, you are on track for budget trouble and it is time to make cuts. This worksheet draws overruns out of the reserve automatically so you can see the burn as it happens instead of at the end.',
  },
  {
    question: 'What do I do if I am already over budget?',
    answer:
      'In order: use the contingency reserve, downgrade finishes you have not bought yet, increase your DIY share on the phases ahead, reduce scope, defer non-essential work until after move-in, and only then look for more funding. The cheapest cuts are always the ones on work that has not started.',
  },
  {
    question: 'What costs do owner-builders forget to budget?',
    answer:
      'Soft costs — permits, impact fees, utility connections, temporary power, dumpsters, tool rental, and builder’s risk insurance — run 8–15% of hard costs and are missing from most first budgets. Site work and landscaping are the other two categories that routinely appear only after the money is spoken for.',
  },
  {
    question: 'Are the numbers I type here saved anywhere?',
    answer:
      'They stay in your own browser so the sheet still has your figures when you come back to it next week. Nothing is sent to a server unless you choose to email yourself a copy. Clearing your browser data or switching devices clears the entries, so keep the real record in a spreadsheet or the binder workbook — this is a check gauge, not your books.',
  },
];

const faqSchema = generateFAQSchema(FAQS);

export default function BudgetTrackerPage() {
  return (
    <div className={s.calcPage}>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: schemaToScriptTag(faqSchema) }}
      />

      <CalcHero
        title="Build Budget Tracker"
        sub="Planned against actual, phase by phase, with the contingency burn in plain sight — so an overrun shows up while you can still do something about it."
        cells={[
          { k: 'Sheet', v: 'W-04' },
          { k: 'Returns', v: 'Variance' },
          { k: 'Scope', v: 'Whole build' },
          { k: 'Basis', v: 'Your figures' },
        ]}
      />

      <div className={s.sheetWrap}>
        <BudgetTrackerCalc />
      </div>

      <div className={s.content}>
        <CalcSection label="Methodology" title="How the variance is figured" meta="SHEET W-04">
          <div className={s.prose}>
            <p>
              <strong>Variance.</strong> Planned minus actual, per phase and for the build as a
              whole. Positive is money still in the plan; negative is an overrun. The sheet shows
              the magnitude with the direction spelled out rather than a signed number, because a
              minus sign in front of a dollar figure is read wrong about half the time.
            </p>
            <p>
              <strong>The 5% band.</strong> A phase counts as on track while it lands within 5% of
              its planned number, over or under. Construction estimates are not precise instruments,
              and treating a 2% miss as a problem trains you to ignore the flags. Past 5% the phase
              is called over or under and the flags fire.
            </p>
            <p>
              <strong>Contingency.</strong> The reserve is a percentage of the planned total, not of
              what you have spent. Only an overrun draws it down — running under budget does not
              build it back above the original reserve, because the money you did not spend on
              framing is not extra insurance, it is just money you have not spent yet.
            </p>
            <p>
              <strong>What the sheet does not do.</strong> It does not estimate anything for you.
              Every number here is one you typed, which is the point: the value is in the comparison
              and the flags, not in the arithmetic. For planning-level numbers to start from, use the{' '}
              <a href="/calculators/material-estimator">whole-house material estimator</a> and price
              the phases you are about to start with real quotes.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Assumptions" title="Bands, reserves, and defaults" meta="ADJUST ABOVE">
          <AssumptionsTable
            rows={[
              { label: 'Variance', value: 'planned − actual' },
              { label: 'On-track band', value: '± 5% of plan' },
              { label: 'Contingency base', value: '% of planned total' },
              { label: 'Contingency draw', value: 'overruns only' },
              { label: 'Low-reserve flag', value: 'under 30% left' },
              { label: 'High-variance flag', value: 'over 15% off plan' },
              { label: 'Sample plan', value: '$250,000 across 6 phases' },
              { label: 'Entries', value: 'stored in your browser' },
            ]}
          />
        </CalcSection>

        <CalcSection label="Context" title="Why budget tracking matters">
          <div className={s.prose}>
            <p>
              <strong>Early warning.</strong> The worst thing that can happen is discovering you are
              over budget when you are 80% done. Tracking budgeted against actual by phase gives you
              warning while costs are only trending high. If the foundation came in 15% over, you
              know immediately to cut finishes or increase the loan — not at the end, when you
              cannot afford cabinets.
            </p>
            <p>
              <strong>Variance analysis.</strong> Understanding where and why you are over or under
              helps you make better decisions on the phases still ahead. Was framing over because
              lumber moved, because the estimate was optimistic, or because the scope grew? Each
              cause calls for a different response. Small early overruns compound: 10% over on
              foundation, framing, and rough-ins leaves you 30% over before finishes.
            </p>
            <p>
              <strong>Contingency management.</strong> Your reserve — typically 10–20% of budget —
              is the safety net. Tracking how much you have used against how much project remains is
              how you gauge risk. Rule of thumb: if you have used more than half the contingency by
              the halfway mark, you are headed for trouble and it is time to cut.
            </p>
            <p>
              <strong>Scope control.</strong> Tracking forces discipline around changes. When you see
              real numbers it is easier to say no to the upgrade. Every small change shows up as
              variance, which makes the cumulative impact visible — and owner-builders are
              particularly prone to adding features mid-build because they are standing right there.
            </p>
            <p>
              <strong>Cash flow.</strong> Knowing actual against budgeted tells you when you will
              need money. Consistently under budget means you can delay draws; over budget means you
              need to arrange funding before you run out. Running out of cash mid-project is
              catastrophic in a way that being over budget on paper is not.
            </p>
            <p>
              <strong>The record afterwards.</strong> Detailed tracking creates a record of what your
              house actually cost, which is worth having for insurance, a future sale, an addition,
              or helping the next owner-builder. It also establishes your cost basis for capital
              gains if you ever sell.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Failure modes" title="Where owner-builder budgets break">
          <div className={s.prose}>
            <p>
              <strong>Optimistic initial budgets.</strong> Most owner-builders start with
              unrealistic numbers: best-case pricing, whole categories forgotten (site work,
              permits, landscaping), and finish costs guessed low. Pad the estimate 10–15% before
              you add contingency on top.
            </p>
            <p>
              <strong>Scope creep.</strong> While we are at it is the most expensive phrase in
              construction. A window here, an upgraded fixture there, and it is thousands. Track
              every change as variance so the cumulative number is visible instead of theoretical.
            </p>
            <p>
              <strong>Material price volatility.</strong> Lumber, concrete, and steel swing 30–100%
              in a year. A budget from six months ago may be fiction. Re-price each phase with
              current quotes before you start it.
            </p>
            <p>
              <strong>Forgotten soft costs.</strong> Permits, impact fees, utility connections,
              temporary power, dumpsters, tool rental, insurance — 8–15% of hard costs, and missing
              from most first drafts.
            </p>
            <p>
              <strong>Rework.</strong> First-time builders make mistakes, failed inspections require
              rework, and changed minds require demolition. Budget 5–10% for the learning curve and
              treat it as a real line item, not bad luck.
            </p>
            <p>
              <strong>Finish fever.</strong> As the house takes shape people get excited and upgrade:
              premium counters, better tile, nicer fixtures. Finish costs routinely exceed budget by
              20–40%. Set the limits early, while the house is still framing and nothing looks
              tempting yet.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Practice" title="How the disciplined ones do it">
          <div className={s.prose}>
            <p>
              <strong>Update weekly.</strong> Enter every expenditure, get quotes for what is coming,
              and adjust the estimates for the phases ahead. Weekly updates catch problems while they
              are still fixable.
            </p>
            <p>
              <strong>Track everything.</strong> Every receipt, every payment, every material run.
              Use a dedicated card or checking account for the build — it makes tracking mechanical
              and keeps construction costs separate from personal spending.
            </p>
            <p>
              <strong>Get three quotes.</strong> For any subcontracted work over $5,000. Three quotes
              validate your budget as much as they get you a price. Compare identical scope and
              identical materials or the comparison is meaningless.
            </p>
            <p>
              <strong>Front-load the contingency.</strong> Spend it on foundation and framing, where
              getting it right matters most. Do not save it for finishes: if you reach finishes under
              budget you can upgrade, and if you are over you can downgrade finishes far more easily
              than you can fix a foundation.
            </p>
            <p>
              <strong>Keep the lender current.</strong> With construction financing, tell your lender
              early when you see overruns coming. Last-minute funding requests are expensive and are
              often declined.
            </p>
            <p>
              <strong>Hold a cash reserve.</strong> Beyond contingency, keep 5–10% of the budget in
              personal cash for timing gaps between draws or an emergency that has nothing to do with
              the house.
            </p>
            <p>
              <strong>Set phase gates.</strong> Before starting a new phase, review the budget. If
              you are over, identify the cuts in the next phase before you commit to the work. It is
              far easier to cut money you have not spent than to claw back money you have.
            </p>
            <p>
              <strong>Track labor separately.</strong> Keep what you paid subs apart from what you
              saved doing the work yourself. That is what tells you whether your{' '}
              <a href="/feasibility/cost-savings-calculator">cost-savings estimate</a> was real, and
              which trades are worth keeping on the next phase.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Recovery" title="When you are over budget, in order">
          <div className={s.prose}>
            <p>
              <strong>1. Use the contingency reserve.</strong> This is what it is for. If you are
              5–10% over on a phase, cover it — then make cuts elsewhere to rebuild the reserve
              before the next phase.
            </p>
            <p>
              <strong>2. Downgrade finishes.</strong> The easiest cuts are on things you have not
              bought. Hardwood to luxury vinyl, granite to laminate, custom cabinets to stock. You
              can upgrade later, after you are living in the house.
            </p>
            <p>
              <strong>3. Do more yourself.</strong> Raise your DIY share on the phases ahead. Paint,
              trim, flooring, and landscaping are DIY-friendly and save 30–50% against hiring out —
              at the cost of weeks on the{' '}
              <a href="/calculators/timeline-estimator">schedule</a>.
            </p>
            <p>
              <strong>4. Reduce scope.</strong> Cut the nice-to-haves: skip the deck, leave the
              basement unfinished, shrink the landscaping. Reduce scope before you cut quality on
              anything structural.
            </p>
            <p>
              <strong>5. Defer work.</strong> Finish to certificate-of-occupancy standard, move in,
              and complete the rest after. Fencing, landscaping, the garage, and the basement can all
              wait until the pressure is off.
            </p>
            <p>
              <strong>6. Increase funding.</strong> Last resort. Additional construction financing, a
              personal loan, or savings — expensive, and worth it only for essential structural work
              you cannot defer or downgrade.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Questions" title="Owner-builders ask" meta="FAQ" noPrint>
          <CalcFAQ items={FAQS.map((f) => ({ question: f.question, answer: f.answer }))} />
        </CalcSection>

        <RelatedCalcs slug="budget-tracker" />

        <div className={`${s.block} ${s.blockLast} no-print`}>
          <BinderCTA
            context="budget-tracker"
            lead="Ready to track a real budget? The Job Site Binder includes an auto-calculating Excel budget workbook — 21 cost categories with live variance and subtotal formulas — plus the printed tracking sheets for the job site."
          />
        </div>
      </div>
    </div>
  );
}
