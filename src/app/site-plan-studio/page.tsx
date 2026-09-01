import Link from 'next/link';
import type { Metadata } from 'next';
import s from '@/styles/SitePlanPage.module.css';
import SitePlanStudio from '@/components/siteplan/SitePlanStudio';
import BinderCTA from '@/components/BinderCTA';
import { generateFAQSchema, schemaToScriptTag } from '@/lib/schema';
import { STATE_KITS } from '@/lib/kits';

export const metadata: Metadata = {
  alternates: { canonical: '/site-plan-studio' },
  title: 'Site Plan Studio — Draw a Site Plan for Your Building Permit',
  description:
    'Draw your lot, house, well, septic and driveway to scale, measure every separation that matters, and print a letter-size plot plan for your permit application — with your state’s published separation rules on the sheet, or the sourced finding of who sets them. Free, no signup.',
};

const FAQS = [
  {
    question: 'Can I draw my own site plan for a building permit?',
    answer:
      'In most rural jurisdictions, yes — and some say so in the ordinance. Wasilla, Alaska expressly lets an owner draw their own site plan for a single-family dwelling or duplex (WMC 16.90.020.B). Colorado puts one- through four-family dwellings outside the architects\' practice act entirely (C.R.S. 12-120-403(1)(a)). But it is a local decision every time: the Municipality of Anchorage requires a surveyed plot plan plus stamped structural calculations for a new home (AMC 23.05.010), and Washington requires the septic design itself to carry a designer\'s name, signature and stamp (WAC 246-272A-0200). Call the counter and ask whether they accept an owner-drawn plan before you spend an afternoon on one.',
  },
  {
    question: 'Does a site plan have to be to scale?',
    answer:
      'Almost always, and it is the single most common reason a hand sketch comes back. A reviewer needs to put a rule on the sheet and confirm your setbacks. Use a standard engineering scale — 1"=10\', 20\', 30\', 40\', 50\', 60\' or 100\' — print it in the title block, and draw a graphic bar scale beside it so the sheet still measures correctly after it has been photocopied at 94%. This tool picks the largest scale that fits your lot on letter paper and prints both.',
  },
  {
    question: 'What is the difference between a site plan and a plot plan?',
    answer:
      'In practice, nothing — most departments use the words interchangeably, and a form asking for a "plot plan" will accept what this tool prints. Where a distinction is drawn, a plot plan shows the parcel, the structures on it and the distances between them, while a site plan adds site work: grading, drainage, utilities, parking and landscaping. A residential owner-builder is almost always being asked for the first one. Neither is a boundary survey.',
  },
  {
    question: 'Do I need a surveyor for my site plan?',
    answer:
      'You need one when the accuracy of a boundary is doing real work: when the house lands close to a setback line, when the recorded lot lines are in doubt or the corner pins cannot be found, when a lender or title company requires a survey, when the parcel is being split or a new legal description is needed, or when the department simply requires a stamped drawing. Away from those, an accurate owner-drawn plan measured from your plat is usually accepted. Drawing it yourself first is worth doing either way — it tells you whether the house fits before you pay anyone.',
  },
  {
    question: 'What separation distances do I need between my well and septic?',
    answer:
      'It depends on the state, and often the state is not the answer. Alaska sets 100 ft from a private well to a septic tank or absorption field by regulation (18 AAC 72.100(a)(1)). Montana sets 50 ft to sealed components and 100 ft to a drainfield (ARM 17.36.323, Table 2). But most states publish no statewide table at all — Michigan has no statewide septic code, California routes it through a local Water Board management program, and Texas, Virginia, Georgia, Kentucky and Mississippi all push the number down to the county. In those states the honest answer is that your county or district health department sets it, and this tool says so instead of drawing a circle it cannot source.',
  },
  {
    question: 'What setbacks should I put on the plan?',
    answer:
      'The ones your zoning ordinance gives you, in writing. Building setbacks are county and municipal, not state, and they vary parcel to parcel with the zoning district, corner-lot rules, overlays and easements — which is why this tool asks you for front, side and rear rather than guessing. Get them from the planning counter before you draw, and ask at the same time whether any critical area, floodplain or wildland-urban-interface overlay touches the parcel, because those buffers move the buildable envelope more than the setbacks do.',
  },
  {
    question: 'What size paper should a site plan be printed on?',
    answer:
      'Letter (8.5×11) is accepted for a straightforward residential parcel at almost every rural counter, and it is what this tool produces — portrait, with a 0.5in margin, a title block, a legend and a bar scale. Larger parcels and anything with engineered site work usually go on 11×17 or 24×36. If your department publishes a submittal checklist, follow it; if it does not, bring letter size and ask whether they want a larger copy before you pay for plotting.',
  },
];

const faqSchema = generateFAQSchema(FAQS);

const SHIPPED_KITS = STATE_KITS.filter((k) => k.status === 'shipped').length;

const CHECKLIST: { key: string; text: string }[] = [
  {
    key: 'Property lines and dimensions',
    text: 'Every boundary, with its length. Take them from your plat or deed, not from a tape measure and a hope.',
  },
  {
    key: 'A north arrow and the scale',
    text: 'Both printed on the sheet. A drawing with no scale cannot be checked, and a drawing with no north cannot be oriented against the parcel map.',
  },
  {
    key: 'The building footprint, dimensioned',
    text: 'The outline of the walls at grade, with overall width and depth. Include decks, porches and roof overhangs if your ordinance measures setbacks to them — many do.',
  },
  {
    key: 'Setbacks from every property line',
    text: 'The distance from each wall to each line, and the required setback beside it. This is the number the reviewer is looking for first.',
  },
  {
    key: 'Every other structure on the parcel',
    text: 'Garage, shop, barn, shed, existing house. Michigan\'s plot-plan rule names "other buildings or structures on the same premises" explicitly.',
  },
  {
    key: 'The well, and the distance to everything',
    text: 'Existing or proposed. Separation distances are measured from it, and a reviewer will look for those numbers rather than compute them.',
  },
  {
    key: 'The septic tank, drainfield and reserve area',
    text: 'The reserve area is not optional decoration — Washington and Michigan both require the replacement area to be shown, and siting the house over it is a classic and expensive mistake.',
  },
  {
    key: 'The driveway and how it meets the road',
    text: 'Including the approach. On unincorporated land the driveway permit is often a separate approval on its own timeline.',
  },
  {
    key: 'Easements and rights-of-way',
    text: 'Utility, access, drainage. They are on your plat and title report, and building across one is a problem no inspection catches until it is expensive.',
  },
  {
    key: 'Surface water, wetlands and slopes',
    text: 'Ponds, streams, lake shore, and any steep bank. Alaska measures 100 ft from a wastewater system to surface water and defines "slough" to include swamp, bog and marsh — which on many parcels is most of the lot.',
  },
];

const TRIGGERS: { key: string; text: string }[] = [
  {
    key: 'The house lands near a line',
    text: 'If any wall is within a few feet of a setback, an unsurveyed drawing is a gamble on where the line actually is. Get the corners located.',
  },
  {
    key: 'The pins cannot be found',
    text: 'No corner monuments, a fence that does not match the plat, or a neighbor who disagrees about the boundary. That is a survey question, not a drawing question.',
  },
  {
    key: 'The department requires a stamp',
    text: 'Anchorage requires a surveyed plot plan for a new home (AMC 23.05.010). Washington requires the septic design to be stamped by its designer (WAC 246-272A-0200). Ask first.',
  },
  {
    key: 'A lender or title company asks',
    text: 'Construction lenders routinely require a survey before the first draw. Finding out at closing is the expensive way.',
  },
  {
    key: 'The parcel is being split',
    text: 'Any new legal description, lot line adjustment or subdivision needs a licensed surveyor by law in every state.',
  },
];

export default function SitePlanStudioPage() {
  return (
    <div className={s.page}>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: schemaToScriptTag(faqSchema) }}
      />

      <section className={`${s.hero} bp-band bp-grid no-print`}>
        <span className={`${s.crop} ${s.tl}`} />
        <span className={`${s.crop} ${s.tr}`} />
        <div className={s.heroInner}>
          <p className={`bp-eyebrow ${s.eyebrow}`}>SP-01 · Site Plan Studio</p>
          <h1 className={s.title}>
            Draw a Site Plan for Your <em>Building Permit</em>
          </h1>
          <p className={s.lead}>
            Draw your lot, house, well, septic and driveway to scale, measure
            every separation that matters, and print a letter-size plot plan for
            your permit application. Where your state publishes separation
            minimums, the tool checks your layout against them, citation and
            all — where it doesn&rsquo;t, the sheet says who does set them, so
            you know exactly which office to call. Free, no signup, nothing
            leaves your browser.
          </p>
          <div className={s.dimstrip}>
            <div className={s.dimcell}>
              <span className={s.k}>Cost</span>
              <span className={s.v}>Free</span>
            </div>
            <div className={s.dimcell}>
              <span className={s.k}>Signup</span>
              <span className={s.v}>None</span>
            </div>
            <div className={s.dimcell}>
              <span className={s.k}>Output</span>
              <span className={s.v}>Print-ready</span>
            </div>
            <div className={s.dimcell}>
              <span className={s.k}>Scale</span>
              <span className={s.v}>To scale</span>
            </div>
          </div>
        </div>
      </section>

      <div className={s.studioWrap}>
        <SitePlanStudio />
      </div>

      <div className={s.content}>
        <section className={s.block}>
          <div className={s.secHead}>
            <div>
              <p className={s.secLabel}>Method</p>
              <h2 className={s.secTitle}>How to draw a site plan for a permit</h2>
            </div>
            <p className={s.secMeta}>Sheet SP-01</p>
          </div>
          <div className={s.prose}>
            <p>
              <strong>Start from your plat, not from memory.</strong> Your
              recorded plat or deed carries the boundary lengths, and your
              county parcel viewer will usually show the same shape with
              dimensions. Those are the numbers to draw from. A tape measure
              across a wooded lot is how a plan ends up three feet out at the
              corner that matters.
            </p>
            <p>
              <strong>Get your setbacks in writing before you draw.</strong> Ask
              the planning counter for front, side and rear for your zoning
              district, and ask in the same call whether a corner-lot rule,
              overlay or easement changes them. Kentucky&apos;s own instruction
              is blunt about this, and many Kentucky jurisdictions require
              zoning approval while issuing no building permit at all — so the
              zoning counter may be the only setback authority you ever meet.
            </p>
            <p>
              <strong>Place the well and the wastewater system first, not
              last.</strong> On a rural parcel these are the constraints that
              decide where the house can go, and they are the ones with
              published minimum distances. Site the drainfield and its reserve
              area, then the well at its separation, then fit the house into
              what is left. Doing it the other way round is how people discover
              that the only spot the septic will perc is under the garage.
            </p>
            <p>
              <strong>Dimension everything a reviewer will want to
              measure.</strong> Each wall to each property line, well to tank,
              well to drainfield, tank to the house. Write the numbers on the
              drawing. A reviewer who has to measure your sheet with a scale is
              a reviewer who can find a reason to send it back.
            </p>
            <p>
              <strong>Print it to scale with a title block.</strong> Standard
              engineering scale, north arrow, a bar scale, and a block naming
              the project, the owner, the address and the parcel number. That is
              what separates a drawing from a sketch, and it is the whole
              purpose of the sheet this tool prints.
            </p>
          </div>
        </section>

        <section className={s.block}>
          <div className={s.secHead}>
            <div>
              <p className={s.secLabel}>Checklist</p>
              <h2 className={s.secTitle}>What to include on a site plan</h2>
            </div>
            <p className={s.secMeta}>10 items</p>
          </div>
          <ol className={s.checklist}>
            {CHECKLIST.map((c) => (
              <li key={c.key} className={s.checkItem}>
                <span>
                  <span className={s.checkKey}>{c.key}</span>
                  <span className={s.checkText}>{c.text}</span>
                </span>
              </li>
            ))}
          </ol>
        </section>

        <section className={s.block}>
          <div className={s.secHead}>
            <div>
              <p className={s.secLabel}>The question behind the question</p>
              <h2 className={s.secTitle}>
                Site plan vs plot plan, and how jurisdictions treat owner-drawn
                plans
              </h2>
            </div>
          </div>
          <div className={s.prose}>
            <p>
              The two words are used interchangeably at almost every counter. If
              a distinction is drawn, a <strong>plot plan</strong> shows the
              parcel, the structures on it and the distances between them, and a{' '}
              <strong>site plan</strong> adds site work — grading, drainage,
              utilities, parking. A residential owner-builder is nearly always
              being asked for the first, whatever the form calls it. Neither one
              is a boundary survey, and no drawing tool can make one.
            </p>
            <p>
              Whether your own drawing is accepted is decided locally, and the
              split can be sharp inside a single state. In Alaska, the City of
              Wasilla expressly permits an owner to draw their own site plan for
              a single-family dwelling or duplex (WMC 16.90.020.B), while the
              Municipality of Anchorage requires a surveyed plot plan and
              stamped structural calculations for a new home (AMC 23.05.010).
              Colorado places one- through four-family dwellings outside the
              architects&apos; practice act (C.R.S. 12-120-403(1)(a)) — so you
              may draw the plans — while leaving it to the building department
              whether an unsurveyed site plan is enough.
            </p>
            <p>
              Two things follow. First, ask before you draw: one phone call
              settles whether you need a surveyor and what the sheet must show.
              Second, the septic side often runs on a separate track from the
              building permit, with its own reviewer and its own timeline —
              Washington requires the septic design to bear its designer&apos;s
              stamp regardless of who draws the building-permit site plan.
            </p>
            <p>
              This tool draws a plan and measures it. It does not survey your
              land, and it does not tell you your permit will be approved. The
              separations it checks are the ones states publish for wells,
              septic tanks and drainfields; setbacks are set by your county or
              city zoning ordinance and vary parcel to parcel, so the tool asks
              you for them rather than guessing. Every rule it checks prints its
              citation on the sheet, so you can hand a reviewer the source
              rather than our word for it.
            </p>
          </div>
        </section>

        <section className={s.block}>
          <div className={s.secHead}>
            <div>
              <p className={s.secLabel}>Big or odd-shaped land</p>
              <h2 className={s.secTitle}>Large or irregular parcel?</h2>
            </div>
            <p className={s.secMeta}>Detail view</p>
          </div>
          <div className={s.prose}>
            <p>
              <strong>A large parcel doesn&rsquo;t need all of itself on the
              sheet.</strong> On acreage, reviewers read the building area, not
              the back forty — at a scale that fits twenty acres on letter
              paper, your house would be smaller than a pencil dot. The
              standard move is a <strong>detail view</strong>: draw a rectangle
              covering just the building site — big enough to hold the house,
              well, septic and their separations — and treat each drawn edge as
              the nearest real boundary line, using the distances from your
              plat. Note the parcel&rsquo;s true size and shape in the
              lot-shape note (it prints on the sheet), and staple your recorded
              plat behind the plan. That pairing — detail drawing plus plat —
              is how large-parcel site plans are routinely submitted.
            </p>
            <p>
              <strong>An odd-shaped lot the tool draws properly.</strong> Tick{' '}
              <em>this lot isn&rsquo;t rectangular</em> in the lot form and draw
              the boundary as it actually runs — click the corners, or enter the
              bearing and distance calls straight off your deed
              (<span className={s.mono}>N 42&deg;15&apos; E</span>,{' '}
              <span className={s.mono}>150.4</span>, one row per call). The tool
              walks the calls, tells you how far the boundary missed closing,
              and closes the gap for you. Every side prints its length the way a
              plat does, and distances to the property line are measured to the
              nearest boundary wherever it bends — so a notched or
              metes-and-bounds parcel gets real numbers instead of a rectangle
              standing in for it. Setback lines stay a rectangle-only feature:
              mitering front, side and rear around an eight-sided boundary is a
              different piece of geometry, and a confidently wrong setback on a
              permit sheet is worse than none.
            </p>
          </div>
        </section>

        <section className={s.block}>
          <div className={s.secHead}>
            <div>
              <p className={s.secLabel}>Know the limit</p>
              <h2 className={s.secTitle}>When you need a surveyor instead</h2>
            </div>
            <p className={s.secMeta}>5 triggers</p>
          </div>
          <div className={s.triggers}>
            {TRIGGERS.map((t) => (
              <div key={t.key} className={s.trigger}>
                <span className={s.triggerKey}>{t.key}</span>
                <p className={s.triggerText}>{t.text}</p>
              </div>
            ))}
          </div>
        </section>

        <section className={s.block}>
          <div className={s.secHead}>
            <div>
              <p className={s.secLabel}>Questions</p>
              <h2 className={s.secTitle}>Owner-builders ask</h2>
            </div>
            <p className={s.secMeta}>FAQ</p>
          </div>
          <div className={s.faqList}>
            {FAQS.map((f) => (
              <div key={f.question} className={s.faqItem}>
                <h3 className={s.faqQ}>{f.question}</h3>
                <p className={s.faqA}>{f.answer}</p>
              </div>
            ))}
          </div>

          <div className={s.seeAlso}>
            <span className={s.seeAlsoKey}>See also</span>
            <Link href="/permitting" className={s.seeAlsoLink}>
              Permitting guide
            </Link>
            <Link href="/permitting/state-guides" className={s.seeAlsoLink}>
              State permit guides
            </Link>
            <Link href="/calculators" className={s.seeAlsoLink}>
              Calculators
            </Link>
            <Link href="/resources/checklists" className={s.seeAlsoLink}>
              Checklists
            </Link>
          </div>
        </section>

        <section className={`${s.block} ${s.blockLast}`}>
          <div className={s.kitBand}>
            <div>
              <p className={s.kitKicker}>Your state, in detail</p>
              <h2 className={s.kitTitle}>
                The plot plan is one sheet of the permit package
              </h2>
              <p className={s.kitCopy}>
                A State Permit Kit is the rest of it: the permit sequence, who
                issues what, the exemptions that do and do not apply to an
                owner-builder, and the traps — with the statute citation printed
                on every page, the same way this sheet prints them.{' '}
                {SHIPPED_KITS} states have shipped kits so far.
              </p>
            </div>
            <div className={s.kitLinks}>
              <Link href="/shop/permit-kits" className={s.kitBtn}>
                See the permit kits — $34
              </Link>
              <p className={s.kitFine}>Instant download · lifetime revisions</p>
            </div>
          </div>

          <BinderCTA
            context="site-plan-studio"
            lead="The plot plan goes at the front of the permit package; the binder is the other 367 pages — inspection logs, subcontractor agreements, quote comparisons, and the tracking sheets that keep a build from becoming a pile of receipts."
          />
        </section>
      </div>
    </div>
  );
}
