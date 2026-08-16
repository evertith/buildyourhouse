import Link from 'next/link';
import type { Metadata } from 'next';
import styles from './contact.module.css';

export const metadata: Metadata = {
  alternates: { canonical: '/contact' },
  title: 'Contact Us — Questions About Building Your Own Home?',
  description: 'Have questions about your owner-builder project? Reach out for guidance on permits, inspections, subcontractors, or any part of the build process.',
};

export default function Contact() {
  return (
    <div className={styles.page}>
      <header className={`${styles.header} bp-band bp-grid`}>
        <span className={`${styles.crop} ${styles.tl}`} />
        <span className={`${styles.crop} ${styles.tr}`} />
        <div className={styles.headerInner}>
          <p className={`bp-eyebrow ${styles.eyebrow}`}>Contact</p>
          <h1>Get In Touch</h1>
          <p className={styles.subtitle}>
            Questions about building your own home? Need to point out something on the site?
            We're here to help.
          </p>
        </div>
      </header>

      <div className={styles.container}>
        <div className={styles.content}>
          <section className={styles.mainSection}>
            <h2>How Can We Help?</h2>

            <div className={styles.contactOptions}>
              <div className={styles.contactCard}>
                <h3>For General Questions</h3>
                <p>
                  Have a general question about owner-building? Want to suggest content for the site?
                  Need clarification on something in our guides?
                </p>
                <a href="mailto:info@build-your-house.com" className={styles.email}>
                  info@build-your-house.com
                </a>
                <p className={styles.note}>
                  <strong>Note:</strong> We receive a lot of email. General questions
                  may be answered in future blog posts or guides.
                </p>
              </div>

              <div className={styles.contactCard}>
                <h3>For Site Issues or Feedback</h3>
                <p>
                  Found a broken link? Have a suggestion for improving the site?
                  Want to share your owner-builder success story?
                </p>
                <a href="mailto:feedback@build-your-house.com" className={styles.email}>
                  feedback@build-your-house.com
                </a>
              </div>

              <div className={styles.contactCard}>
                <h3>For Media & Partnership Inquiries</h3>
                <p>
                  Press inquiries, podcast interviews, or professional partnerships.
                </p>
                <a href="mailto:media@build-your-house.com" className={styles.email}>
                  media@build-your-house.com
                </a>
              </div>
            </div>
          </section>

          <section className={styles.faqSection}>
            <h2>Before You Email...</h2>
            <p>Check if your question is already answered:</p>

            <div className={styles.faqList}>
              <div className={styles.faqItem}>
                <h4>"Is owner-building right for me?"</h4>
                <p>
                  Start with our <Link href="/feasibility/is-it-right-for-you">self-assessment guide</Link> and
                  the <Link href="/start-here">Start Here</Link> page.
                </p>
              </div>

              <div className={styles.faqItem}>
                <h4>"How much can I really save?"</h4>
                <p>
                  Use our <Link href="/feasibility/cost-savings-calculator">cost savings calculator</Link> to
                  get a realistic estimate based on your project.
                </p>
              </div>

              <div className={styles.faqItem}>
                <h4>"How do I find good subcontractors?"</h4>
                <p>
                  Read our comprehensive guide on <Link href="/subcontractors/finding-quality-subs">finding and vetting subs</Link>.
                </p>
              </div>

              <div className={styles.faqItem}>
                <h4>"What does the permit process look like?"</h4>
                <p>
                  Check out our <Link href="/permitting">complete permitting guide</Link> and
                  <Link href="/permitting/state-guides">state-specific resources</Link>.
                </p>
              </div>

              <div className={styles.faqItem}>
                <h4>"Where can I find templates and tools?"</h4>
                <p>
                  Visit our <Link href="/resources">resources page</Link> for templates, checklists,
                  calculators, and other helpful tools.
                </p>
              </div>
            </div>
          </section>

          <section className={styles.responseSection}>
            <h2>What to Expect</h2>

            <div className={styles.expectations}>
              <div className={styles.expectationItem}>
                <h3>Response Time</h3>
                <p>
                  <strong>General questions:</strong> Within 3-5 business days
                </p>
                <p>
                  <strong>Site feedback:</strong> We read everything, though we may not respond to all feedback emails
                </p>
              </div>

              <div className={styles.expectationItem}>
                <h3>What We Can Help With</h3>
                <ul>
                  <li>General owner-building guidance and strategy</li>
                  <li>Clarification on content from the site</li>
                  <li>Suggestions for new content or tools</li>
                  <li>Site issues or technical problems</li>
                  <li>Media and partnership opportunities</li>
                </ul>
              </div>

              <div className={styles.expectationItem}>
                <h3>What We Can't Help With (Via Email)</h3>
                <ul>
                  <li>Detailed plan reviews</li>
                  <li>Specific problem diagnosis on your project</li>
                  <li>Emergency on-site issues (contact a local contractor)</li>
                  <li>Acting as your contractor of record</li>
                  <li>Local code interpretations (contact your building department)</li>
                </ul>
              </div>
            </div>
          </section>

          <section className={styles.socialSection}>
            <h2>Connect on Social Media</h2>
            <p>
              Follow along for tips, updates, and real stories from owner-builders:
            </p>
            <div className={styles.socialLinks}>
              <a href="#" className={styles.socialLink}>
                <span className={styles.socialIcon}>📘</span>
                Facebook
                <span className={styles.placeholder}>[link placeholder]</span>
              </a>
              <a href="#" className={styles.socialLink}>
                <span className={styles.socialIcon}>📸</span>
                Instagram
                <span className={styles.placeholder}>[link placeholder]</span>
              </a>
              <a href="#" className={styles.socialLink}>
                <span className={styles.socialIcon}>🐦</span>
                Twitter/X
                <span className={styles.placeholder}>[link placeholder]</span>
              </a>
              <a href="#" className={styles.socialLink}>
                <span className={styles.socialIcon}>▶️</span>
                YouTube
                <span className={styles.placeholder}>[link placeholder]</span>
              </a>
              <a href="#" className={styles.socialLink}>
                <span className={styles.socialIcon}>💼</span>
                LinkedIn
                <span className={styles.placeholder}>[link placeholder]</span>
              </a>
            </div>
            <p className={styles.socialNote}>
              <em>Social media accounts coming soon. Email is the best way to reach us for now.</em>
            </p>
          </section>

          <section className={styles.ctaSection}>
            <h2>Ready to Start Building?</h2>
            <p>
              Not sure where to begin? Start with these resources:
            </p>
            <div className={styles.ctaLinks}>
              <Link href="/start-here" className={styles.ctaButton}>
                Start Here Guide
              </Link>
              <Link href="/feasibility/is-it-right-for-you" className={styles.ctaButton}>
                Is It Right for You?
              </Link>
              <Link href="/resources" className={styles.ctaButton}>
                Resources
              </Link>
            </div>
          </section>
        </div>

        <footer className={styles.disclaimer}>
          <p>
            <strong>Important:</strong> Email communication does not establish a client relationship or
            create professional liability. For legal terms governing this website, see our <Link href="/terms">Terms of Use</Link>.
          </p>
        </footer>
      </div>
    </div>
  );
}
