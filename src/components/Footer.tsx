import Link from 'next/link';
import styles from '@/styles/Footer.module.css';

export default function Footer() {
  const currentYear = new Date().getFullYear();

  return (
    <footer className={styles.footer}>
      <div className={styles.container}>
        <div className={styles.columns}>
          <div className={styles.column}>
            <h3>Get Started</h3>
            <ul className={styles.links}>
              <li><Link href="/start-here">Start Here</Link></li>
              <li><Link href="/feasibility/is-it-right-for-you">Is It Right For You?</Link></li>
              <li><Link href="/feasibility/cost-savings-calculator">Cost Savings Calculator</Link></li>
              <li><Link href="/feasibility/state-by-state-rules">State Rules</Link></li>
            </ul>
          </div>

          <div className={styles.column}>
            <h3>Critical Guides</h3>
            <ul className={styles.links}>
              <li><Link href="/permitting">Permitting Guide</Link></li>
              <li><Link href="/inspections">Inspections</Link></li>
              <li><Link href="/subcontractors">Finding Subs</Link></li>
              <li><Link href="/timing-and-scheduling">Scheduling</Link></li>
            </ul>
          </div>

          <div className={styles.column}>
            <h3>Resources</h3>
            <ul className={styles.links}>
              <li><Link href="/calculators">Calculators</Link></li>
              <li><Link href="/resources/checklists">Checklists</Link></li>
              <li><Link href="/resources/templates">Templates</Link></li>
              <li><Link href="/resources/glossary">Glossary</Link></li>
            </ul>
          </div>

          <div className={styles.column}>
            <h3>Connect</h3>
            <ul className={styles.links}>
              <li><Link href="/blog">Blog</Link></li>
              <li><Link href="/consulting">Consulting</Link></li>
              <li><Link href="/about">About</Link></li>
              <li><Link href="/contact">Contact</Link></li>
            </ul>
          </div>
        </div>

        <div className={styles.bottom}>
          <p className={styles.tagline}>
            Built with expertise by a retired general contractor
          </p>
          <p className={styles.disclaimer}>
            <strong>Disclaimer:</strong> This site provides general information only. Building codes,
            regulations, and requirements vary by location. Always consult with licensed professionals
            and verify with your local building department before starting any construction project.
          </p>
          <p className={styles.copyright}>
            © {currentYear} Build-Your-House.com. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
}
