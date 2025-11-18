import Link from 'next/link';
import type { Metadata } from 'next';
import styles from './start-here.module.css';

export const metadata: Metadata = {
  title: 'Start Here - Owner-Builder Roadmap | Build-Your-House.com',
  description: 'Complete roadmap for building your own home. Learn the step-by-step process from planning to completion.',
};

export default function StartHere() {
  return (
    <div className={styles.container}>
      <article className={styles.article}>
        <header className={styles.header}>
          <h1>Start Here: Your Owner-Builder Roadmap</h1>
          <p className={styles.intro}>
            Building your own home is one of the most rewarding projects you'll ever undertake.
            This guide will walk you through every phase, from initial planning to moving in.
          </p>
        </header>

        <section className={styles.section}>
          <h2>The Complete Owner-Builder Process</h2>
          <p>
            Most owner-builders take 12-18 months to complete their home. Here's the roadmap:
          </p>

          <div className={styles.roadmap}>
            <div className={styles.phase}>
              <div className={styles.phaseNumber}>1</div>
              <div className={styles.phaseContent}>
                <h3>Feasibility Assessment (Week 1-2)</h3>
                <p>Before you commit, determine if owner-building is right for you.</p>
                <ul>
                  <li><Link href="/feasibility/is-it-right-for-you">Take the self-assessment quiz</Link></li>
                  <li><Link href="/feasibility/cost-savings-calculator">Calculate your potential savings</Link></li>
                  <li><Link href="/feasibility/time-commitment">Understand the time commitment</Link></li>
                  <li><Link href="/feasibility/state-by-state-rules">Check your state's requirements</Link></li>
                </ul>
              </div>
            </div>

            <div className={styles.phase}>
              <div className={styles.phaseNumber}>2</div>
              <div className={styles.phaseContent}>
                <h3>Planning Phase (Month 1-3)</h3>
                <p>Set yourself up for success with proper planning.</p>
                <ul>
                  <li><Link href="/planning/secure-land">Secure land</Link> (if you don't have it)</li>
                  <li><Link href="/planning/financing">Get financing/construction loan approved</Link></li>
                  <li><Link href="/planning/house-plans">Choose or design your house plans</Link></li>
                  <li><Link href="/planning/budget">Create detailed budget</Link></li>
                  <li><Link href="/planning/timeline">Develop project timeline</Link></li>
                </ul>
              </div>
            </div>

            <div className={styles.phase}>
              <div className={styles.phaseNumber}>3</div>
              <div className={styles.phaseContent}>
                <h3>Permitting (Month 2-4)</h3>
                <p>Navigate the building department and get permits approved.</p>
                <ul>
                  <li><Link href="/permitting/understanding-building-codes">Learn building codes basics</Link></li>
                  <li><Link href="/permitting/permit-application-process">Submit permit application</Link></li>
                  <li><Link href="/permitting/working-with-building-department">Build relationships with inspectors</Link></li>
                  <li><Link href="/permitting/common-permit-mistakes">Avoid common mistakes</Link></li>
                </ul>
              </div>
            </div>

            <div className={styles.phase}>
              <div className={styles.phaseNumber}>4</div>
              <div className={styles.phaseContent}>
                <h3>Find & Vet Subcontractors (Month 2-4)</h3>
                <p>Line up quality subs before breaking ground.</p>
                <ul>
                  <li><Link href="/subcontractors/when-to-hire-vs-diy">Decide what to DIY vs hire</Link></li>
                  <li><Link href="/subcontractors/finding-quality-subs">Find quality subcontractors</Link></li>
                  <li><Link href="/subcontractors/vetting-and-interviewing">Vet and interview candidates</Link></li>
                  <li><Link href="/subcontractors/contracts-and-agreements">Create contracts</Link></li>
                </ul>
              </div>
            </div>

            <div className={styles.phase}>
              <div className={styles.phaseNumber}>5</div>
              <div className={styles.phaseContent}>
                <h3>Construction (Month 4-16)</h3>
                <p>The actual building process, phase by phase.</p>
                <ul>
                  <li><Link href="/build-phases/site-preparation">Site Preparation</Link> (1-2 weeks)</li>
                  <li><Link href="/build-phases/foundation">Foundation</Link> (2-4 weeks)</li>
                  <li><Link href="/build-phases/framing">Framing</Link> (4-8 weeks)</li>
                  <li><Link href="/build-phases/roofing">Roofing</Link> (1-2 weeks)</li>
                  <li><Link href="/build-phases/rough-in">Rough-in (Plumbing, Electrical, HVAC)</Link> (3-6 weeks)</li>
                  <li><Link href="/build-phases/insulation">Insulation</Link> (1-2 weeks)</li>
                  <li><Link href="/build-phases/drywall">Drywall</Link> (2-4 weeks)</li>
                  <li><Link href="/build-phases/finish">Finish Work</Link> (6-12 weeks)</li>
                </ul>
              </div>
            </div>

            <div className={styles.phase}>
              <div className={styles.phaseNumber}>6</div>
              <div className={styles.phaseContent}>
                <h3>Inspections Throughout</h3>
                <p>Pass inspections at every critical phase.</p>
                <ul>
                  <li><Link href="/inspections/foundation-inspection">Foundation Inspection</Link></li>
                  <li><Link href="/inspections/framing-inspection">Framing Inspection</Link></li>
                  <li><Link href="/inspections/rough-in-inspections">Rough-in Inspections</Link></li>
                  <li><Link href="/inspections/final-inspection">Final Inspection</Link></li>
                </ul>
              </div>
            </div>

            <div className={styles.phase}>
              <div className={styles.phaseNumber}>7</div>
              <div className={styles.phaseContent}>
                <h3>Move In & Celebrate!</h3>
                <p>Final walkthrough, certificate of occupancy, and enjoy your new home.</p>
                <ul>
                  <li><Link href="/move-in/punch-list">Complete punch list items</Link></li>
                  <li><Link href="/move-in/certificate-of-occupancy">Get certificate of occupancy</Link></li>
                  <li><Link href="/move-in/loan-conversion">Convert construction loan to mortgage</Link></li>
                  <li><Link href="/move-in/moving-in">Move in and enjoy the fruits of your labor</Link></li>
                </ul>
              </div>
            </div>
          </div>
        </section>

        <section className={styles.section}>
          <h2>What You'll Save</h2>
          <div className={styles.savings}>
            <div className={styles.savingsCard}>
              <h3>General Contractor Fee</h3>
              <div className={styles.amount}>$30,000 - $100,000+</div>
              <p>Typical GC fees are 15-20% of construction cost</p>
            </div>
            <div className={styles.savingsCard}>
              <h3>Your Labor Value</h3>
              <div className={styles.amount}>$20,000 - $50,000</div>
              <p>Value of work you do yourself vs hiring out</p>
            </div>
            <div className={styles.savingsCard}>
              <h3>Total Potential Savings</h3>
              <div className={styles.amount}>$50,000 - $150,000+</div>
              <p>On a $300,000-$500,000 home</p>
            </div>
          </div>
          <div className={styles.cta}>
            <Link href="/feasibility/cost-savings-calculator" className={styles.button}>
              Calculate Your Exact Savings
            </Link>
          </div>
        </section>

        <section className={styles.section}>
          <h2>Essential Resources</h2>
          <div className={styles.resources}>
            <Link href="/calculators" className={styles.resourceCard}>
              <h3>Calculators</h3>
              <p>Estimate costs, materials, and timeline</p>
            </Link>
            <Link href="/resources/checklists" className={styles.resourceCard}>
              <h3>Checklists</h3>
              <p>Never forget a critical step</p>
            </Link>
            <Link href="/resources/templates" className={styles.resourceCard}>
              <h3>Templates</h3>
              <p>Contracts, budgets, schedules</p>
            </Link>
            <Link href="/resources" className={styles.resourceCard}>
              <h3>Resources</h3>
              <p>Guides, tools, and downloads</p>
            </Link>
          </div>
        </section>

        <section className={styles.callout}>
          <h2>Ready to Begin?</h2>
          <p>
            Start with the feasibility assessment to make sure owner-building is the right choice for you.
          </p>
          <Link href="/feasibility/is-it-right-for-you" className={styles.button}>
            Take the Assessment
          </Link>
        </section>
      </article>
    </div>
  );
}
