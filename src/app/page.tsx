import Link from 'next/link';
import type { Metadata } from "next";
import Icon, { type IconName } from '@/components/Icon';
import styles from './page.module.css';

export const metadata: Metadata = {
  alternates: { canonical: '/' },
  title: 'Build Your Own House — Step-by-Step Owner-Builder Guide',
  description: 'A retired general contractor with 15+ years of experience shows you exactly how to build your own home. Free calculators, checklists, permit guides, and phase-by-phase instructions.',
};

const SHEETS: { no: string; icon: IconName; title: string; href: string; desc: string }[] = [
  { no: 'A-01', icon: 'permit', title: 'Permitting & Inspections', href: '/permitting', desc: 'Navigate the permit process, pass inspections on the first try, and work effectively with building departments.' },
  { no: 'A-02', icon: 'subs', title: 'Finding Subcontractors', href: '/subcontractors', desc: "Find, vet, hire, and manage quality subs — and learn which trades you can legally DIY on your own home." },
  { no: 'A-03', icon: 'schedule', title: 'Timing & Scheduling', href: '/timing-and-scheduling', desc: 'Build realistic timelines, dodge the common delays, and coordinate multiple trades without stalling the job.' },
  { no: 'A-04', icon: 'phases', title: 'Build Phases', href: '/build-phases', desc: 'Step-by-step playbooks for every phase, from site prep and foundation to framing and final finishes.' },
  { no: 'A-05', icon: 'tools', title: 'Tools & Equipment', href: '/tools-and-equipment', desc: "The tools that actually earn their keep, buy-vs-rent break-evens, and the safety gear you can't skip." },
  { no: 'A-06', icon: 'calculator', title: 'Calculators & Tools', href: '/calculators/material-estimator', desc: 'Cost-savings calculator, material estimator, timeline planner, and a budget tracker that flags overruns.' },
];

const NOTES: { n: string; h: string; p: string }[] = [
  { n: '01', h: 'Real experience', p: "A retired GC who's built custom homes. Not theory — this is what actually works on a real job site." },
  { n: '02', h: 'Honest advice', p: 'What can go wrong, what costs more than you think, and exactly when you should hire help instead.' },
  { n: '03', h: 'Specific numbers', p: 'Real costs, realistic timelines, and actual code references — checked against the statutes, not vague generalities.' },
  { n: '04', h: 'Kept current', p: 'Codes and material costs change. The guides are reviewed and updated against the latest requirements.' },
];

export default function Home() {
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
              <div className={styles.eyebrow}>Sheet 01 — Start Here</div>
              <h1 className={styles.heroTitle}>Build your own house — and save <em>tens of thousands.</em></h1>
              <p className={styles.heroSub}>
                Owner-builders who stay organized save roughly 10–25% of project cost by skipping the GC markup
                (though lost contractor discounts and overruns can eat into that). The complete field guide — from
                a retired general contractor with 15+ years on the job.
              </p>
              <div className={styles.heroCtas}>
                <Link href="/start-here" className={styles.btnPrimary}>Start the Guide →</Link>
                <Link href="/feasibility/cost-savings-calculator" className={styles.btnGhost}>Calculate Your Savings</Link>
              </div>
            </div>
            <aside className={styles.specsheet}>
              <div className={styles.sheetNo}><span>Project Specs</span><span>Rev. 2026</span></div>
              <div className={styles.dimrow}><span className={styles.k}>Typical Savings</span><span className={styles.v}><em>10–25%</em></span></div>
              <div className={styles.dimrow}><span className={styles.k}>State Guides</span><span className={styles.v}>50</span></div>
              <div className={styles.dimrow}><span className={styles.k}>Build Phases</span><span className={styles.v}>16</span></div>
              <div className={styles.dimrow}><span className={styles.k}>GC Experience</span><span className={styles.v}>15<small>yr</small></span></div>
            </aside>
          </div>
        </div>
      </section>

      {/* INTRO STRIP */}
      <div className={styles.strip}>
        <div className={styles.stripInner}>
          <span className={styles.who}>From the desk of<br />a retired GC</span>
          <p className={styles.lead}>
            &ldquo;You don&rsquo;t need to be a contractor — you need to be organized, persistent, and willing to learn.
            Here&rsquo;s everything I wish every owner-builder knew before breaking ground.&rdquo;
          </p>
        </div>
      </div>

      {/* SHEETS / INDEX */}
      <section className={styles.block}>
        <div className={styles.wrap}>
          <div className={styles.secHead}>
            <div>
              <div className={styles.num}>02 / Index</div>
              <h2 className={styles.secTitle}>Essential owner-builder guides</h2>
            </div>
            <div className={styles.secMeta}>Drawn to scale<br />Verified · 2026</div>
          </div>
          <div className={styles.sheets}>
            {SHEETS.map((s) => (
              <Link key={s.no} href={s.href} className={styles.sheet}>
                <span className={styles.sno}>{s.no}</span>
                <Icon name={s.icon} size={38} className={styles.ico} />
                <h3 className={styles.sheetTitle}>{s.title}</h3>
                <p className={styles.sheetDesc}>{s.desc}</p>
                <span className={styles.go}>Open Sheet <span className={styles.arr}>→</span></span>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* FIELD NOTES */}
      <div className={styles.notesWrap}>
        <div className={styles.wrap}>
          <div className={styles.notes}>
            <div className={styles.notesLeft}>
              <div className={styles.num}>03 / Field Notes</div>
              <h2 className={styles.notesTitle}>Why trust this guide?</h2>
              <p className={styles.notesIntro}>No fluff, no upsell. Just what a working general contractor would tell you over the tailgate.</p>
              <span className={styles.stamp}>Verified · Code-Checked</span>
            </div>
            <div className={styles.notesRight}>
              {NOTES.map((note) => (
                <div key={note.n} className={styles.note}>
                  <span className={styles.nn}>{note.n}</span>
                  <div>
                    <h4 className={styles.noteH}>{note.h}</h4>
                    <p className={styles.noteP}>{note.p}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* CTA BAND */}
      <section className={styles.ctaBand}>
        <div className={styles.ctaInner}>
          <div className={styles.eyebrow}>Sheet 04 — Break Ground</div>
          <h2 className={styles.ctaTitle}>Ready to build the house you&rsquo;ve been drawing in your head?</h2>
          <p className={styles.ctaSub}>Start with the roadmap that takes you from feasibility study to final certificate of occupancy.</p>
          <div className={styles.heroCtas}>
            <Link href="/start-here" className={styles.btnPrimary}>Start Here →</Link>
            <Link href="/permitting/state-guides" className={styles.btnGhost}>Browse State Guides</Link>
          </div>
        </div>
      </section>
    </div>
  );
}
