import Link from 'next/link';
import type { Metadata } from 'next';
import Icon, { type IconName } from '@/components/Icon';
import BinderCTA from '@/components/BinderCTA';
import styles from './start-here.module.css';

export const metadata: Metadata = {
  alternates: { canonical: '/start-here' },
  title: 'Start Here — Your Owner-Builder Roadmap From Day 1 to Move-In',
  description: 'The complete owner-builder roadmap. Where to start, what order to tackle things, and the step-by-step path from idea to moving into your new home.',
};

type PhaseLink = { href: string; label: string; note?: string };
type Phase = { no: string; sheet: string; icon: IconName; title: string; when: string; blurb: string; links: PhaseLink[] };

const PHASES: Phase[] = [
  {
    no: '01', sheet: 'PH-01', icon: 'compass', title: 'Feasibility Assessment', when: 'Week 1–2',
    blurb: 'Before you commit, determine if owner-building is right for you.',
    links: [
      { href: '/feasibility/is-it-right-for-you', label: 'Take the self-assessment quiz' },
      { href: '/feasibility/cost-savings-calculator', label: 'Calculate your potential savings' },
      { href: '/feasibility/time-commitment', label: 'Understand the time commitment' },
      { href: '/feasibility/state-by-state-rules', label: "Check your state's requirements" },
    ],
  },
  {
    no: '02', sheet: 'PH-02', icon: 'ruler', title: 'Planning Phase', when: 'Month 1–3',
    blurb: 'Set yourself up for success with proper planning.',
    links: [
      { href: '/planning/secure-land', label: 'Secure land', note: "if you don't have it" },
      { href: '/planning/financing', label: 'Get financing / construction loan approved' },
      { href: '/planning/house-plans', label: 'Choose or design your house plans' },
      { href: '/planning/budget', label: 'Create detailed budget' },
      { href: '/planning/timeline', label: 'Develop project timeline' },
      { href: '/timing-and-scheduling/material-lead-times', label: 'Plan material lead times', note: 'order 2–4 months ahead' },
    ],
  },
  {
    no: '03', sheet: 'PH-03', icon: 'permit', title: 'Permitting', when: 'Month 2–4',
    blurb: 'Navigate the building department and get permits approved.',
    links: [
      { href: '/permitting/understanding-building-codes', label: 'Learn building codes basics' },
      { href: '/permitting/permit-application-process', label: 'Submit permit application' },
      { href: '/permitting/working-with-building-department', label: 'Build relationships with inspectors' },
      { href: '/permitting/common-permit-mistakes', label: 'Avoid common mistakes' },
    ],
  },
  {
    no: '04', sheet: 'PH-04', icon: 'subs', title: 'Find & Vet Subcontractors', when: 'Month 2–4',
    blurb: 'Line up quality subs before breaking ground.',
    links: [
      { href: '/subcontractors/when-to-hire-vs-diy', label: 'Decide what to DIY vs hire' },
      { href: '/subcontractors/finding-quality-subs', label: 'Find quality subcontractors' },
      { href: '/subcontractors/vetting-and-interviewing', label: 'Vet and interview candidates' },
      { href: '/subcontractors/contracts-and-agreements', label: 'Create contracts' },
    ],
  },
  {
    no: '05', sheet: 'PH-05', icon: 'phases', title: 'Construction', when: 'Month 4–16',
    blurb: 'The actual building process, phase by phase.',
    links: [
      { href: '/build-phases/site-preparation', label: 'Site Preparation', note: '1–2 weeks' },
      { href: '/build-phases/foundation', label: 'Foundation', note: '2–4 weeks' },
      { href: '/build-phases/framing', label: 'Framing', note: '4–8 weeks' },
      { href: '/build-phases/roofing', label: 'Roofing', note: '1–2 weeks' },
      { href: '/build-phases/rough-in', label: 'Rough-in (Plumbing, Electrical, HVAC)', note: '3–6 weeks' },
      { href: '/build-phases/insulation', label: 'Insulation', note: '1–2 weeks' },
      { href: '/build-phases/drywall', label: 'Drywall', note: '2–4 weeks' },
      { href: '/build-phases/interior-trim', label: 'Interior Trim', note: '2–3 weeks' },
      { href: '/build-phases/finish', label: 'Finish Work', note: '6–12 weeks' },
    ],
  },
  {
    no: '06', sheet: 'PH-06', icon: 'check', title: 'Inspections', when: 'Throughout',
    blurb: 'Pass inspections at every critical phase.',
    links: [
      { href: '/inspections/foundation-inspection', label: 'Foundation Inspection' },
      { href: '/inspections/framing-inspection', label: 'Framing Inspection' },
      { href: '/inspections/rough-in-inspections', label: 'Rough-in Inspections' },
      { href: '/inspections/final-inspection', label: 'Final Inspection' },
    ],
  },
  {
    no: '07', sheet: 'PH-07', icon: 'doc', title: 'Move In & Celebrate', when: 'Move-in',
    blurb: 'Final walkthrough, certificate of occupancy, and enjoy your new home.',
    links: [
      { href: '/move-in/punch-list', label: 'Complete punch list items' },
      { href: '/move-in/certificate-of-occupancy', label: 'Get certificate of occupancy' },
      { href: '/move-in/loan-conversion', label: 'Convert construction loan to mortgage' },
      { href: '/move-in/moving-in', label: 'Move in and enjoy the fruits of your labor' },
    ],
  },
];

const SAVINGS: { label: string; amount: string; accent?: boolean; note: string }[] = [
  { label: 'General Contractor Fee', amount: '$30,000–$100,000+', note: 'Typical GC fees are 15–20% of construction cost.' },
  { label: 'Your Labor Value', amount: '$20,000–$50,000', note: 'Value of work you do yourself vs. hiring out.' },
  { label: 'Total Potential Savings', amount: '~10–25%', accent: true, note: 'Of project cost, best case, on a $300,000–$500,000 home.' },
];

const RESOURCES: { href: string; icon: IconName; title: string; desc: string }[] = [
  { href: '/calculators', icon: 'calculator', title: 'Calculators', desc: 'Estimate costs, materials, and timeline.' },
  { href: '/resources/checklists', icon: 'check', title: 'Checklists', desc: 'Never forget a critical step.' },
  { href: '/resources/templates', icon: 'doc', title: 'Templates', desc: 'Contracts, budgets, schedules.' },
  { href: '/resources', icon: 'tools', title: 'Resources', desc: 'Guides, tools, and downloads.' },
];

export default function StartHere() {
  return (
    <div className={styles.page}>
      {/* HERO */}
      <section className={styles.hero}>
        <span className={`${styles.crop} ${styles.tl}`} />
        <span className={`${styles.crop} ${styles.tr}`} />
        <span className={`${styles.crop} ${styles.bl}`} />
        <span className={`${styles.crop} ${styles.br}`} />
        <div className={styles.heroInner}>
          <div className={styles.heroGrid}>
            <div>
              <div className={styles.eyebrow}>Owner-Builder Roadmap</div>
              <h1 className={styles.heroTitle}>Your roadmap, <em>day one to move-in.</em></h1>
              <p className={styles.heroSub}>
                Building your own home is one of the most rewarding projects you&rsquo;ll ever undertake.
                This guide walks you through every phase &mdash; from the first feasibility check to the day you turn the key.
              </p>
              <div className={styles.heroCtas}>
                <Link href="/feasibility/is-it-right-for-you" className={styles.btnPrimary}>Take the Assessment →</Link>
                <Link href="/feasibility/cost-savings-calculator" className={styles.btnGhost}>Calculate Your Savings</Link>
              </div>
            </div>
            <aside className={styles.specsheet}>
              <div className={styles.sheetNo}><span>Project Specs</span><span>Rev. 2026</span></div>
              <div className={styles.dimrow}><span className={styles.k}>Timeline</span><span className={styles.v}>12–18<small>mo</small></span></div>
              <div className={styles.dimrow}><span className={styles.k}>Roadmap Phases</span><span className={styles.v}>07</span></div>
              <div className={styles.dimrow}><span className={styles.k}>Build Phases</span><span className={styles.v}>08</span></div>
              <div className={styles.dimrow}><span className={styles.k}>Typical Savings</span><span className={styles.v}><em>10–25%</em></span></div>
            </aside>
          </div>
        </div>
      </section>

      {/* ROADMAP */}
      <section className={styles.block}>
        <div className={styles.wrap}>
          <div className={styles.secHead}>
            <div>
              <div className={styles.num}>01 / Roadmap</div>
              <h2 className={styles.secTitle}>The complete owner-builder process</h2>
            </div>
            <div className={styles.secMeta}>12–18 months<br />7 phases</div>
          </div>
          <p className={styles.lead}>Most owner-builders take 12&ndash;18 months to complete their home. Here&rsquo;s the path, in order:</p>

          <ol className={styles.roadmap}>
            {PHASES.map((p) => (
              <li key={p.no} className={styles.phase}>
                <div className={styles.phaseMarker}>
                  <span className={styles.phaseNo}>{p.no}</span>
                  <span className={styles.phaseSheet}>{p.sheet}</span>
                </div>
                <div className={styles.phaseBody}>
                  <div className={styles.phaseHead}>
                    <Icon name={p.icon} size={26} className={styles.phaseIco} />
                    <h3 className={styles.phaseTitle}>{p.title}</h3>
                    <span className={styles.when}>{p.when}</span>
                  </div>
                  <p className={styles.phaseBlurb}>{p.blurb}</p>
                  <ul className={styles.phaseLinks}>
                    {p.links.map((l) => (
                      <li key={l.href}>
                        <Link href={l.href} className={styles.phaseLink}>
                          <span className={styles.tick} aria-hidden="true" />
                          <span>{l.label}</span>
                        </Link>
                        {l.note && <span className={styles.linkNote}>{l.note}</span>}
                      </li>
                    ))}
                  </ul>
                </div>
              </li>
            ))}
          </ol>
        </div>
      </section>

      {/* SAVINGS */}
      <div className={styles.savingsWrap}>
        <div className={styles.wrap}>
          <div className={styles.secHead}>
            <div>
              <div className={styles.num}>02 / Economics</div>
              <h2 className={styles.secTitle}>What you&rsquo;ll save</h2>
            </div>
            <div className={styles.secMeta}>Estimate only<br />Net of overruns</div>
          </div>
          <div className={styles.savings}>
            {SAVINGS.map((s) => (
              <div key={s.label} className={styles.savingsCard}>
                <span className={styles.savingsLabel}>{s.label}</span>
                <span className={`${styles.amount} ${s.accent ? styles.amountAccent : ''}`}>{s.amount}</span>
                <p className={styles.savingsNote}>{s.note}</p>
              </div>
            ))}
          </div>
          <p className={styles.savingsCaveat}>
            <strong>A reality check:</strong> those two figures overlap, so don&rsquo;t simply stack them. Owner-builders also tend to give
            some savings back&mdash;through the bulk-buying and trade discounts a GC gets, plus the cost overruns that come
            with learning on the job. Plan for a realistic net of roughly 10&ndash;25% of project cost, not a guaranteed windfall.
          </p>
          <div className={styles.cta}>
            <Link href="/feasibility/cost-savings-calculator" className={styles.btnPrimaryDark}>Calculate Your Potential Savings →</Link>
          </div>
        </div>
      </div>

      {/* RESOURCES */}
      <section className={styles.block}>
        <div className={styles.wrap}>
          <div className={styles.secHead}>
            <div>
              <div className={styles.num}>03 / Toolkit</div>
              <h2 className={styles.secTitle}>Essential resources</h2>
            </div>
            <div className={styles.secMeta}>Free downloads<br />Updated 2026</div>
          </div>
          <div className={styles.resources}>
            {RESOURCES.map((r) => (
              <Link key={r.href} href={r.href} className={styles.resourceCard}>
                <Icon name={r.icon} size={30} className={styles.resIco} />
                <h3 className={styles.resTitle}>{r.title}</h3>
                <p className={styles.resDesc}>{r.desc}</p>
                <span className={styles.go}>Open <span className={styles.arr}>→</span></span>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* BINDER CROSS-SELL */}
      <section className={styles.block}>
        <div className={styles.wrap}>
          <BinderCTA
            context="start-here"
            lead="Prefer everything in one place from day one? The Job Site Binder collects the checklists, contracts, and tracking sheets for every phase on this roadmap — 367 print-ready pages, organized the way a GC organizes a job."
          />
        </div>
      </section>

      {/* CTA BAND */}
      <section className={styles.ctaBand}>
        <div className={styles.ctaInner}>
          <div className={styles.eyebrow}>Sheet 00 — Break Ground</div>
          <h2 className={styles.ctaTitle}>Ready to begin?</h2>
          <p className={styles.ctaSub}>
            Start with the feasibility assessment to make sure owner-building is the right choice for you.
          </p>
          <div className={styles.heroCtas}>
            <Link href="/feasibility/is-it-right-for-you" className={styles.btnPrimary}>Take the Assessment →</Link>
            <Link href="/permitting/state-guides" className={styles.btnGhost}>Browse State Guides</Link>
          </div>
        </div>
      </section>
    </div>
  );
}
