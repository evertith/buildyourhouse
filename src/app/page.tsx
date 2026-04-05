import Link from 'next/link';
import styles from './page.module.css';
import type { Metadata } from "next";
import EmailCapture from '@/components/EmailCapture';

export const metadata: Metadata = {
  title: 'Build Your Own House & Save $50K-$150K+ — Step-by-Step Owner-Builder Guide',
  description: 'Retired GC shows you exactly how to build your own home. Free calculators, checklists, permit guides for all 50 states, and phase-by-phase instructions. Start planning today.',
};

export default function Home() {
  return (
    <div className={styles.page}>
      {/* Hero Section */}
      <section className={styles.hero}>
        <h1 className={styles.heroTitle}>
          Build Your Own House and Save $50,000+
        </h1>
        <p className={styles.heroSubtitle}>
          Complete guide from a retired general contractor with 15+ years experience helping owner-builders succeed
        </p>
        <div className={styles.heroCtas}>
          <Link href="/start-here" className={styles.buttonPrimary}>
            Start Here
          </Link>
          <Link href="/feasibility/cost-savings-calculator" className={styles.buttonSecondary}>
            Calculate Your Savings
          </Link>
        </div>
      </section>

      {/* Introduction */}
      <section className={styles.intro}>
        <div className={styles.introContent}>
          <p className={styles.lead}>
            Building your own home is one of the biggest financial and emotional decisions you'll ever make.
            You don't need to be a contractor—you need to be organized, persistent, and willing to learn.
          </p>
          <p>
            I'm a retired general contractor who's built custom homes. This site contains everything I wish
            every owner-builder knew before starting: the real costs, realistic timelines, and honest advice about what
            you can DIY and what you should hire out.
          </p>
        </div>
      </section>

      {/* Main Topic Cards */}
      <section className={styles.topics}>
        <h2 className={styles.sectionTitle}>Essential Owner-Builder Guides</h2>
        <div className={styles.topicGrid}>
          <Link href="/permitting" className={styles.card}>
            <div className={styles.cardIcon}>📋</div>
            <h3 className={styles.cardTitle}>Permitting & Inspections</h3>
            <p className={styles.cardDescription}>
              Navigate the permitting process, pass inspections on first try, and work effectively with building departments
            </p>
            <span className={styles.cardLink}>Learn More →</span>
          </Link>

          <Link href="/subcontractors" className={styles.card}>
            <div className={styles.cardIcon}>👷</div>
            <h3 className={styles.cardTitle}>Finding Subcontractors</h3>
            <p className={styles.cardDescription}>
              Find, vet, hire, and manage quality subs who'll help you build your dream home
            </p>
            <span className={styles.cardLink}>Learn More →</span>
          </Link>

          <Link href="/timing-and-scheduling" className={styles.card}>
            <div className={styles.cardIcon}>📅</div>
            <h3 className={styles.cardTitle}>Timing & Scheduling</h3>
            <p className={styles.cardDescription}>
              Create realistic timelines, avoid common delays, and coordinate multiple trades efficiently
            </p>
            <span className={styles.cardLink}>Learn More →</span>
          </Link>

          <Link href="/build-phases" className={styles.card}>
            <div className={styles.cardIcon}>🏗️</div>
            <h3 className={styles.cardTitle}>Build Phases</h3>
            <p className={styles.cardDescription}>
              Step-by-step guides for each phase from site prep to final finishes
            </p>
            <span className={styles.cardLink}>Learn More →</span>
          </Link>

          <Link href="/tools-and-equipment" className={styles.card}>
            <div className={styles.cardIcon}>🔨</div>
            <h3 className={styles.cardTitle}>Tools & Equipment</h3>
            <p className={styles.cardDescription}>
              Essential tools, buy vs rent analysis, and safety equipment requirements
            </p>
            <span className={styles.cardLink}>Learn More →</span>
          </Link>

          <Link href="/calculators/material-estimator" className={styles.card}>
            <div className={styles.cardIcon}>🧮</div>
            <h3 className={styles.cardTitle}>Calculators & Tools</h3>
            <p className={styles.cardDescription}>
              Cost savings calculator, material estimator, timeline planner, and budget tracker
            </p>
            <span className={styles.cardLink}>Use Tools →</span>
          </Link>
        </div>
      </section>

      {/* Why Trust This Guide */}
      <section className={styles.trust}>
        <div className={styles.trustContent}>
          <h2 className={styles.trustTitle}>Why Trust This Guide?</h2>
          <div className={styles.trustGrid}>
            <div className={styles.trustPoint}>
              <div className={styles.trustIcon}>✓</div>
              <div>
                <h3>Real Experience</h3>
                <p>Retired GC who's built custom homes. Not theory—this is what actually works.</p>
              </div>
            </div>

            <div className={styles.trustPoint}>
              <div className={styles.trustIcon}>✓</div>
              <div>
                <h3>Honest Advice</h3>
                <p>I'll tell you what can go wrong, what will cost more than you think, and when to hire help.</p>
              </div>
            </div>

            <div className={styles.trustPoint}>
              <div className={styles.trustIcon}>✓</div>
              <div>
                <h3>Specific Numbers</h3>
                <p>Real costs, realistic timelines, and actual code references—not vague generalities.</p>
              </div>
            </div>

            <div className={styles.trustPoint}>
              <div className={styles.trustIcon}>✓</div>
              <div>
                <h3>Updated Regularly</h3>
                <p>Building codes and material costs change. This guide stays current with the latest requirements.</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Email Capture - above footer */}
      <EmailCapture source="homepage" />

      {/* CTA Section */}
      <section className={styles.cta}>
        <h2>Ready to Start Your Owner-Builder Journey?</h2>
        <p className={styles.ctaDescription}>
          Begin with our comprehensive roadmap that covers everything from feasibility to final inspection.
        </p>
        <div className={styles.ctaButtons}>
          <Link href="/start-here" className={styles.buttonPrimary}>
            Start Here
          </Link>
          <Link href="/pricing" className={styles.buttonSecondary}>
            See Pricing Plans
          </Link>
        </div>
      </section>
    </div>
  );
}
