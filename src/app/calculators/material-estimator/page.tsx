import type { Metadata } from 'next';
import { Instrument_Sans, Instrument_Serif } from 'next/font/google';
import s from '@/styles/CalcSheet.module.css';
import Estimator from '@/components/estimate/Estimator';
import { CalcSection, AssumptionsTable, CalcFAQ, RelatedCalcs } from '@/components/calc/sections';
import BinderCTA from '@/components/BinderCTA';
import { generateFAQSchema, schemaToScriptTag } from '@/lib/schema';
import { DEFAULT_ALL_HIRED, DEFAULT_ESTIMATE, defaultPhase, roundDollar, roundK } from '@/lib/estimate/defaults';
import { PROFILE_DEFAULTS } from '@/lib/estimate/geometry';
import { CONTINGENCY_SHARE, FINISH_MULTIPLIER, PRICES_AS_OF } from '@/lib/estimate/prices';
import { HOURLY_RATE, LABOR_RATIO } from '@/lib/estimate/labor';
import type { PhaseId } from '@/lib/estimate/types';
import { STUDTALLY_PRICE } from '@/lib/studtally';

// Scoped to this page's root: the rest of the site keeps Fraunces and Hanken Grotesk.
const instrumentSerif = Instrument_Serif({
  subsets: ['latin'],
  weight: '400',
  style: ['normal', 'italic'],
  display: 'swap',
  variable: '--ff-est-serif',
});
const instrumentSans = Instrument_Sans({
  subsets: ['latin'],
  weight: ['400', '500', '600', '700'],
  display: 'swap',
  variable: '--ff-est-sans',
});

export const metadata: Metadata = {
  alternates: { canonical: '/calculators/material-estimator' },
  title: 'Cost to Build a House Calculator: Every Phase, Materials and Labor',
  description:
    'What it costs to build a house, phase by phase, from your square footage: materials and labor shown apart, a Hire it or Do it myself switch on every phase, and a state index that moves the numbers. Free, no signup.',
};

// Every number cited below comes from the engine's default run, so a price
// refresh moves the copy with the ledger.
const D = DEFAULT_ESTIMATE;
const H = DEFAULT_ALL_HIRED;
const SQFT = PROFILE_DEFAULTS.heatedSf.toLocaleString('en-US');
const allHired = roundK(H.totals.allHired.mid);
const allHiredLow = roundK(H.totals.cash.low);
const allHiredHigh = roundK(H.totals.cash.high);
const perSf = roundDollar(H.totals.perSqFt.mid);
const cashDiy = roundK(D.totals.cash.mid);
const diyHours = Math.round(D.totals.hours / 10) * 10;
const laborPct = Math.round((H.totals.hiredLabor.mid / H.totals.allHired.mid) * 100);
const hiredLabor = roundK(H.totals.hiredLabor.mid);
const materials = roundK(H.totals.materials.mid);
const softCosts = roundK(H.totals.soft.mid);
const framing = defaultPhase('framing');
const framingTotal = roundK(
  (framing.materials.low + framing.materials.high + framing.labor.low + framing.labor.high) / 2
);
const framingHours = Math.round(framing.hours / 10) * 10;
const lineQty = (phase: PhaseId, id: string) => {
  const l = defaultPhase(phase).lines.find((x) => x.id === id);
  return l ? Math.round(l.qty).toLocaleString('en-US') : '—';
};
const ASSUMED_LABELS = ['Footprint', 'Walls', 'Openings', 'Rooms', 'Roof', 'Foundation', 'Porch'];

const FAQS = [
  {
    question: `How much does it cost to build a ${SQFT} sq ft house?`,
    answer: `With every trade hired, this calculator puts a ${SQFT} sq ft one-story house on a slab with standard finishes in North Carolina at about ${allHired}, or ${perSf} a square foot, with a likely range of ${allHiredLow} to ${allHiredHigh}. That is cash to build: materials, hired labor, and the soft costs before you break ground, without the land, the loan, or a contingency. Do the insulation, interior finish, and final phase yourself, as the ledger starts out, and cash drops to about ${cashDiy} for roughly ${diyHours.toLocaleString('en-US')} hours of your own work. Change the state and the index moves every line.`,
  },
  {
    question: 'How much of the cost of building a house is labor?',
    answer: `About ${laborPct}% in the default house: ${hiredLabor} of ${allHired} is hired labor, ${materials} is materials, and ${softCosts} is permits, fees, insurance, and plans. That split is the whole case for owner-building. You cannot talk a lumberyard down by half, but you can replace a crew with your own hours on the phases you are able to do, and the ledger shows what each one is worth. Framing alone is about ${framingTotal} hired, or ${framingHours.toLocaleString('en-US')} hours of yours.`,
  },
  {
    question: 'Which phases can I do myself?',
    answer:
      'Anything the ledger lets you flip, with two cautions. Plumbing, electrical, and HVAC are licensed trades in many states, and some require a licensed contractor to pull the permit even on a house you own; those three rows carry a note, and your state guide has the rule. And framing, roofing, and drywall are hard, fast work on a schedule, so price your own hours honestly: the ledger converts each phase to hours at a crew rate, and a first-timer takes longer than the crew.',
  },
  {
    question: `What does the $${STUDTALLY_PRICE} at StudTally buy?`,
    answer: `The framing list only. StudTally reads your plan set and returns every stud, plate, header, sheet, and hanger, counted per wall and reviewed by a person, as the list the lumberyard keys in. It does not price the other thirteen phases; those stay estimates from this page. Use it when you are ready to order framing, not to budget the house.`,
  },
  {
    question: 'How big can the plan PDF be for StudTally?',
    answer:
      '100 MB and 40 sheets. A full set from an architect is usually well under that; if yours is not, export the PDF at a lower raster resolution or send only the architectural sheets (plans, elevations, sections, schedules), which are the ones that get read.',
  },
  {
    question: 'Why is my quote different from this estimate?',
    answer:
      'Three reasons, in order of size. Prices move: lumber swings 50 to 100% with the market, so a quote from a different quarter is a different number. Your lot is not the typical one: rock, a steep grade, a long drive, or a well and septic in place of a tap fee each move a phase by thousands. And a contractor account at a real lumberyard beats big-box retail by 10 to 20%, the easiest discount an owner-builder can pick up. Use the ledger to size the budget and sanity-check quotes, not to replace them.',
  },
  {
    question: 'How accurate is a square-footage estimate?',
    answer:
      'Close enough to budget with, not close enough to order from. The ledger derives a footprint, walls, openings, and a roof from your square footage by the rules stated below, so an unusual shape, a walk-out basement, or a lot of glass will move the numbers. Once you have plans, the trade sheets (framing lumber, concrete, drywall, roofing, flooring, insulation) take real dimensions and give you order quantities, and StudTally reads the plan set itself for the framing list.',
  },
  {
    question: 'What does this estimate leave out?',
    answer:
      'The land and everything about buying it, the construction loan and its interest, and the furniture. It also assumes a buildable lot with utilities at the street: a well and septic, a long power run, rock, or fill beyond the allowance are on top. Carry the 10% contingency the rail shows; every build finds something.',
  },
];

const faqSchema = generateFAQSchema(FAQS);

export default function MaterialEstimatorPage() {
  const g = D.geometry;
  return (
    <div className={s.calcPage}>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: schemaToScriptTag(faqSchema) }}
      />

      <Estimator fontClass={`${instrumentSerif.variable} ${instrumentSans.variable}`} />

      <div className={s.content}>
        <CalcSection label="Methodology" title="How the ledger is figured" meta="SHEET W-02">
          <div className={s.prose}>
            <p>
              Everything starts from one division: finished square footage ÷ stories = footprint.
              The footprint is treated as a 1.5:1 rectangle for wall lengths, openings and rooms are
              counted by density rules, and the roof is drawn over the footprint, the garage, and
              the porch. Those few derived numbers feed every phase, each of which prices a short
              list of real line items at national rates as of {PRICES_AS_OF}, scaled by the state
              you pick. Open any row on the ledger to see its lines; the defaults below are for the{' '}
              {SQFT} sq ft house.
            </p>
            <p>
              <strong>Before you break ground.</strong> The building permit is a state base plus
              $0.35 per heated square foot, with plan review, the survey, the water and sewer tap
              or impact fees (the state table carries the band), twelve months of builder&apos;s
              risk insurance at half a percent of the hard cost, and the plans. Paid, not built, so
              there is no labor switch.
            </p>
            <p>
              <strong>Site work.</strong> Fill and topsoil, a 100-ft gravel drive at 8 in deep,
              silt fence around the disturbed area, a stone construction entrance, and a temporary
              power pole. Clearing and grading are equipment and labor, which is why this phase
              carries the highest labor ratio on the ledger.
            </p>
            <p>
              <strong>Foundation.</strong> A slab is 4 in over the house and garage with a
              20 × 12 in turned-down footing, mesh, rebar in the footing, a vapor barrier, and 4 in
              of gravel ({lineQty('foundation', 'concrete')} yd³ in the default house, with a 10%
              order factor). A crawl space swaps that for a continuous footing, a 3-ft block stem
              wall, piers every 200 sq ft, a treated sill, and vents, and the first floor becomes
              framed. A basement is 8-ft poured walls on footings with a slab, waterproofing, and
              drain tile. The{' '}
              <a href="/calculators/concrete-slab">concrete slab calculator</a> prices a pour from
              your actual dimensions.
            </p>
            <p>
              <strong>Framing.</strong> The same conventions as the{' '}
              <a href="/calculators/framing-lumber">framing lumber calculator</a>: one stud per
              linear foot of wall at 16 in on center, three runs of plate in 16-ft sticks, a
              doubled header per opening, 4 × 8 OSB with 10% waste, house wrap, then joists and
              subfloor for any framed floor, trusses at 2 ft on center over the plan area, roof
              sheathing, porch posts, and allowances for blocking and fasteners. The default house
              takes {lineQty('framing', 'ext-studs')} exterior studs,{' '}
              {lineQty('framing', 'int-studs')} partition studs, and{' '}
              {lineQty('framing', 'trusses')} trusses.
            </p>
            <p>
              <strong>Roofing.</strong> Sloped area is the plan area times the pitch factor
              (6:12 by default), with 10, 15, or 20% waste by how cut up the roof is; three
              bundles per square ({lineQty('roofing', 'shingles')} in the default house),
              synthetic underlayment, ice and water on the eaves, starter, cap, drip edge, ridge
              vent, flashing, and nails, as the{' '}
              <a href="/calculators/roofing">roofing calculator</a> counts them.
            </p>
            <p>
              <strong>Windows and exterior doors.</strong> One window per 110 sq ft at 15 sq ft
              each, an entry door with sidelights, a patio door, a back door, and a 16-ft garage
              door with its opener when the house is large enough to carry a garage. Finish level
              moves these: basic is {FINISH_MULTIPLIER.basic}× the standard rate, premium{' '}
              {FINISH_MULTIPLIER.premium}×.
            </p>
            <p>
              <strong>Exterior finish.</strong> Fiber-cement lap siding on the wall area after
              openings with 10% waste, trim at corners, openings, and the band, soffit and fascia on
              the eaves and rakes, aluminum gutters with four downspouts, and a caulk-and-flashing
              allowance. Finish-sensitive.
            </p>
            <p>
              <strong>Plumbing, electrical, HVAC.</strong> Plumbing is priced per fixture for the
              rough-in (three per bath, two in the kitchen, two in the laundry, two hose bibs) plus
              the service lines, water heater, and finish fixtures. Electrical is a 200-amp
              service, wire and boxes per heated square foot, devices and a fixture allowance per
              room, and detectors. HVAC is a heat pump at one ton per 600 sq ft, moved by the
              state&apos;s climate, with ductwork per square foot, a thermostat, and bath fans.
              These three carry a licensed-trade note because many states require one.
            </p>
            <p>
              <strong>Insulation, drywall, paint.</strong> R-19 batts in the walls and blown
              fiberglass to R-49 in the attic by the{' '}
              <a href="/calculators/insulation">insulation calculator</a>&apos;s bag charts, with
              floor batts under a crawl space or rigid foam on basement walls. Board is the{' '}
              <a href="/calculators/drywall">drywall calculator</a>&apos;s 3.7 × floor area
              ({lineQty('drywallPaint', 'board')} sheets in the default house) with compound, tape,
              screws, and corner bead; paint is the{' '}
              <a href="/calculators/paint">paint calculator</a>&apos;s primer plus two coats at
              350 sq ft per gallon, with trim enamel per room.
            </p>
            <p>
              <strong>Interior finish and final.</strong> Interior doors are rooms minus two;
              baseboard runs the finished wall perimeter; flooring is the heated area with 8% waste
              at a blended plank, tile, and carpet rate (the{' '}
              <a href="/calculators/flooring">flooring calculator</a> does it by room); cabinets,
              vanities, countertops, bath tile, shower glass, and accessories are counted by kitchen
              and bath. The final phase is the appliance package, 870 sq ft of concrete drive and
              walks, seed and shrubs, the last clean, three dumpsters, and the odds and ends.
            </p>
            <p>
              <strong>Labor and the state index.</strong> Each phase&apos;s labor is its material
              cost times a ratio calibrated to 2026 subcontractor quotes (framing{' '}
              {LABOR_RATIO.framing}, drywall and paint {LABOR_RATIO.drywallPaint}, electrical{' '}
              {LABOR_RATIO.electrical}, openings {LABOR_RATIO.openings}), then the state&apos;s
              labor index. Hours are that figure at a blended crew rate of ${HOURLY_RATE.framing} an
              hour (${HOURLY_RATE.plumbing} for the licensed trades). The materials index is narrow,
              since lumber and concrete travel; the labor index is wide, since crews do not. North
              Carolina is 1.00. The permit base and tap fees are set per state and are not scaled
              again.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Assumptions" title="What the default house assumes" meta="CHANGE THE CHIPS">
          <AssumptionsTable
            rows={[
              ...g.assumed.map((a, i) => ({ label: ASSUMED_LABELS[i] ?? 'Also', value: a })),
              {
                label: 'Finish multiplier',
                value: `Basic ${FINISH_MULTIPLIER.basic}×, standard 1×, premium ${FINISH_MULTIPLIER.premium}× on openings, exterior, drywall and paint, interior`,
              },
              {
                label: 'Labor ratios',
                value: `Site ${LABOR_RATIO.site}, foundation ${LABOR_RATIO.foundation}, framing ${LABOR_RATIO.framing}, roofing ${LABOR_RATIO.roofing}, plumbing ${LABOR_RATIO.plumbing}, electrical ${LABOR_RATIO.electrical}, HVAC ${LABOR_RATIO.hvac}, drywall and paint ${LABOR_RATIO.drywallPaint}, interior ${LABOR_RATIO.interior}, final ${LABOR_RATIO.final}`,
              },
              { label: 'Contingency', value: `${Math.round(CONTINGENCY_SHARE * 100)}% of cash to build, shown apart` },
              { label: 'Prices', value: `National ranges, ${PRICES_AS_OF}; the ledger prints the middle of each range` },
            ]}
          />
        </CalcSection>

        <CalcSection label="Scope" title="What this estimate leaves out">
          <div className={s.prose}>
            <p>
              The land, the loan, and the furniture. The ledger also assumes a buildable lot with
              utilities at the street and a typical footprint; a well and septic, a long power run,
              rock, extra fill, a retaining wall, or an unusual shape are on top. Track what you
              actually spend against the phases in the{' '}
              <a href="/calculators/budget-tracker">budget tracker</a>, and carry the contingency.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Field notes" title="Ordering materials without losing money">
          <div className={s.prose}>
            <p>
              <strong>Order 10–15% extra on anything you cut.</strong> Waste, mistakes, and future
              repairs all come out of the same pile. It matters most for materials that get
              discontinued — flooring, tile, siding — where a matching board three years from now is
              worth more than the storage space it took.
            </p>
            <p>
              <strong>Open contractor accounts.</strong> Set up accounts at real lumberyards and
              suppliers rather than buying retail. Better pricing (usually 10–20% off), delivery
              scheduling, and access to contractor-grade material that the big boxes do not stock.
              This is the largest discount available to an owner-builder for the least effort.
            </p>
            <p>
              <strong>Time orders to the schedule, not the budget.</strong> Bring material in 1–2
              weeks before you need it. Buying everything up front invites theft, weather damage,
              and ties up cash you will want later. The exception is lumber: if the market is low
              and you have dry covered storage, locking a price in is defensible. Sequence your
              orders against your{' '}
              <a href="/calculators/timeline-estimator">build timeline</a> and the{' '}
              <a href="/build-phases/framing">framing phase</a> in particular, since that is where
              the biggest single delivery lands.
            </p>
            <p>
              <strong>Inspect every delivery before you sign.</strong> Count it, look for damage,
              check that it is what you ordered. Getting credit after the driver pulls away is a
              different and much worse conversation.
            </p>
            <p>
              <strong>Store it like it cost you money.</strong> Wet lumber warps, wet drywall is
              scrap, and moisture-damaged material causes problems that surface a year later. Tarps
              on, material up off the dirt, stacked flat.
            </p>
            <p>
              <strong>Keep every receipt.</strong> Track each purchase against the phase it belongs
              to. You will need it for budget tracking, for warranty claims, and occasionally for an
              inspector who wants to see a product spec.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Questions" title="Owner-builders ask" meta="FAQ" noPrint>
          <CalcFAQ items={FAQS.map((f) => ({ question: f.question, answer: f.answer }))} />
        </CalcSection>

        <RelatedCalcs slug="material-estimator" />

        <div className={`${s.block} ${s.blockLast} no-print`}>
          <BinderCTA
            context="material-estimator"
            lead="Costing the house is planning-phase work — and it's exactly what the Job Site Binder's Excel calculators do with live formulas: concrete, drywall, paint, and roofing, plus 367 print-ready pages of checklists and logs for when the build starts."
          />
        </div>
      </div>
    </div>
  );
}
