import Link from 'next/link';
import type { Metadata } from 'next';
import styles from './contact.module.css';

export const metadata: Metadata = {
  title: 'Contact Us - Get Owner-Builder Guidance | Build-Your-House.com',
  description: 'Have questions about building your own home? Get in touch with our retired general contractor for guidance, consulting services, or general inquiries.',
};

export default function Contact() {
  return (
    <div className={styles.page}>
      <div className={styles.container}>
        <header className={styles.header}>
          <h1>Get In Touch</h1>
          <p className={styles.subtitle}>
            Questions about building your own home? Want to discuss consulting services?
            Or just need to point out something on the site? We're here to help.
          </p>
        </header>

        <div className={styles.content}>
          <section className={styles.mainSection}>
            <h2>How Can We Help?</h2>

            <div className={styles.contactOptions}>
              <div className={styles.contactCard}>
                <h3>For Consulting Services</h3>
                <p>
                  Interested in one-on-one consulting, plan reviews, or project oversight?
                  Check out our consulting services page for details on what we offer and pricing.
                </p>
                <Link href="/consulting" className={styles.button}>
                  View Consulting Services
                </Link>
                <p className={styles.orText}>Or email us directly:</p>
                <a href="mailto:consulting@build-your-house.com" className={styles.email}>
                  consulting@build-your-house.com
                </a>
              </div>

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
                  <strong>Note:</strong> We receive a lot of email. For specific project questions
                  that require professional review, please use our consulting services. General questions
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
                <h4>"Can you review my plans or answer specific questions about my project?"</h4>
                <p>
                  Yes! That's what our <Link href="/consulting">consulting services</Link> are for.
                  For project-specific professional advice, we offer plan reviews and phone consultations.
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
                  <strong>Consulting inquiries:</strong> Within 24-48 hours
                </p>
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
                  <li>Consulting service questions and scheduling</li>
                  <li>Clarification on content from the site</li>
                  <li>Suggestions for new content or tools</li>
                  <li>Site issues or technical problems</li>
                  <li>Media and partnership opportunities</li>
                </ul>
              </div>

              <div className={styles.expectationItem}>
                <h3>What We Can't Help With (Via Email)</h3>
                <ul>
                  <li>Detailed plan reviews (requires paid consultation)</li>
                  <li>Specific problem diagnosis on your project (requires consultation)</li>
                  <li>Emergency on-site issues (contact a local contractor)</li>
                  <li>Acting as your contractor of record</li>
                  <li>Local code interpretations (contact your building department)</li>
                  <li>Product recommendations for commission (we don't do affiliate marketing)</li>
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

          <section className={styles.locationSection}>
            <h2>Location & Service Area</h2>
            <p>
              <strong>Primary License:</strong> [State placeholder - update with your actual state and license number]
            </p>
            <p>
              <strong>Consulting Services:</strong> Available nationwide (remote consultation)
            </p>
            <p>
              <strong>On-Site Visits:</strong> [Primary service area placeholder - e.g., "Within 100 miles of Charlotte, NC" or "By arrangement, travel fees apply"]
            </p>
            <p>
              While my license is specific to [State], the building code guidance on this site applies to most U.S.
              locations since the majority of jurisdictions use the International Residential Code (IRC) as their base.
              State-specific differences are noted in our <Link href="/permitting/state-guides">state guides</Link>.
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
              <Link href="/consulting" className={styles.ctaButton}>
                Consulting Services
              </Link>
            </div>
          </section>
        </div>

        <footer className={styles.disclaimer}>
          <p>
            <strong>Important:</strong> Email communication does not establish a client relationship or
            create professional liability. For professional consulting services with formal engagement,
            see our <Link href="/consulting">consulting services page</Link>. For legal terms governing
            this website, see our <Link href="/terms">Terms of Service</Link>.
          </p>
        </footer>
      </div>
    </div>
  );
}
