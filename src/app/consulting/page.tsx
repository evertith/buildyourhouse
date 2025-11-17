import Link from 'next/link';
import type { Metadata } from 'next';
import styles from './consulting.module.css';

export const metadata: Metadata = {
  title: 'Owner-Builder Consulting Services - Expert Guidance for Your Build',
  description: 'Get personalized guidance from a retired general contractor. Plan reviews, phone consultations, and project oversight for owner-builders.',
};

export default function Consulting() {
  return (
    <div className={styles.page}>
      <div className={styles.container}>
        <header className={styles.header}>
          <h1>Owner-Builder Consulting Services</h1>
          <p className={styles.subtitle}>
            Get personalized guidance from a retired general contractor with years of experience
            building custom homes. Available for plan reviews, consultations, and ongoing support.
          </p>
        </header>

        <section className={styles.services}>
          <div className={styles.serviceCard}>
            <div className={styles.serviceHeader}>
              <h2>Plan Review</h2>
              <div className={styles.price}>$500</div>
            </div>
            <div className={styles.serviceContent}>
              <p className={styles.serviceDescription}>
                Before you submit for permits, have an experienced GC review your plans for
                common issues and cost-saving opportunities.
              </p>
              <h4>What's Included:</h4>
              <ul>
                <li>Complete review of architectural plans</li>
                <li>Identification of potential code issues</li>
                <li>Cost-saving suggestions</li>
                <li>Buildability assessment</li>
                <li>Written report with recommendations</li>
                <li>One follow-up call to discuss findings</li>
              </ul>
              <div className={styles.timeline}>
                <strong>Timeline:</strong> 3-5 business days
              </div>
              <a href="mailto:consulting@build-your-house.com?subject=Plan Review" className={styles.button}>
                Request Plan Review
              </a>
            </div>
          </div>

          <div className={styles.serviceCard + ' ' + styles.featured}>
            <div className={styles.badge}>Most Popular</div>
            <div className={styles.serviceHeader}>
              <h2>Phone Consultation</h2>
              <div className={styles.price}>$200/hour</div>
            </div>
            <div className={styles.serviceContent}>
              <p className={styles.serviceDescription}>
                One-on-one phone consultation to answer your specific questions and provide
                guidance on your owner-builder project.
              </p>
              <h4>Great For:</h4>
              <ul>
                <li>Getting started and planning your approach</li>
                <li>Solving specific construction problems</li>
                <li>Subcontractor vetting and selection</li>
                <li>Inspection preparation</li>
                <li>Budget and timeline planning</li>
                <li>Troubleshooting issues that arise</li>
              </ul>
              <div className={styles.timeline}>
                <strong>Scheduling:</strong> Usually within 48 hours
              </div>
              <a href="mailto:consulting@build-your-house.com?subject=Phone Consultation" className={styles.button}>
                Schedule Consultation
              </a>
            </div>
          </div>

          <div className={styles.serviceCard}>
            <div className={styles.serviceHeader}>
              <h2>On-Site Visit</h2>
              <div className={styles.price}>Starting at $1,500</div>
            </div>
            <div className={styles.serviceContent}>
              <p className={styles.serviceDescription}>
                In-person site visit to assess your project, meet your team, and provide
                detailed guidance.
              </p>
              <h4>What's Included:</h4>
              <ul>
                <li>Full site walkthrough and assessment</li>
                <li>Review work in progress</li>
                <li>Meet with subcontractors</li>
                <li>Identify issues before inspection</li>
                <li>Detailed written report</li>
                <li>Follow-up phone call included</li>
              </ul>
              <div className={styles.timeline}>
                <strong>Note:</strong> Price varies by location and project scope
              </div>
              <a href="mailto:consulting@build-your-house.com?subject=On-Site Visit" className={styles.button}>
                Inquire About Visit
              </a>
            </div>
          </div>

          <div className={styles.serviceCard}>
            <div className={styles.serviceHeader}>
              <h2>Monthly Project Oversight</h2>
              <div className={styles.price}>$500/month</div>
            </div>
            <div className={styles.serviceContent}>
              <p className={styles.serviceDescription}>
                Weekly check-ins throughout your build. Get ongoing support, answer questions
                as they arise, and keep your project on track.
              </p>
              <h4>What's Included:</h4>
              <ul>
                <li>Weekly 30-minute check-in calls</li>
                <li>Email/text support between calls</li>
                <li>Schedule and budget tracking</li>
                <li>Pre-inspection reviews (via photos/video)</li>
                <li>Subcontractor contract reviews</li>
                <li>Peace of mind throughout your build</li>
              </ul>
              <div className={styles.timeline}>
                <strong>Commitment:</strong> Minimum 3 months
              </div>
              <a href="mailto:consulting@build-your-house.com?subject=Monthly Oversight" className={styles.button}>
                Get Started
              </a>
            </div>
          </div>

          <div className={styles.serviceCard + ' ' + styles.premium}>
            <div className={styles.serviceHeader}>
              <h2>Complete Project Oversight</h2>
              <div className={styles.price}>$5,000+</div>
            </div>
            <div className={styles.serviceContent}>
              <p className={styles.serviceDescription}>
                Full project management from planning through completion. Like having a GC,
                but you maintain control and save money.
              </p>
              <h4>What's Included:</h4>
              <ul>
                <li>Plan review and permit assistance</li>
                <li>Help finding and vetting subcontractors</li>
                <li>Contract negotiations and reviews</li>
                <li>Full schedule management</li>
                <li>Budget tracking and cost control</li>
                <li>On-site visits at critical phases</li>
                <li>Inspection preparation and attendance</li>
                <li>Problem-solving throughout build</li>
              </ul>
              <div className={styles.timeline}>
                <strong>Note:</strong> Price varies by project size and complexity
              </div>
              <a href="mailto:consulting@build-your-house.com?subject=Complete Oversight" className={styles.button}>
                Discuss Your Project
              </a>
            </div>
          </div>
        </section>

        <section className={styles.why}>
          <h2>Why Work With Us?</h2>
          <div className={styles.benefits}>
            <div className={styles.benefit}>
              <h3>Licensed & Experienced</h3>
              <p>
                Licensed general contractor with years of experience building hundreds of
                custom homes. We've seen it all.
              </p>
            </div>
            <div className={styles.benefit}>
              <h3>Owner-Builder Focused</h3>
              <p>
                We specialize in helping owner-builders succeed. We understand your unique
                challenges and goals.
              </p>
            </div>
            <div className={styles.benefit}>
              <h3>Practical Advice</h3>
              <p>
                No-nonsense, practical guidance based on real-world experience. We'll tell
                you what works and what doesn't.
              </p>
            </div>
            <div className={styles.benefit}>
              <h3>Cost-Effective</h3>
              <p>
                Our fees are a fraction of what you'd pay a full-service GC, and the value
                of catching one mistake can pay for itself many times over.
              </p>
            </div>
          </div>
        </section>

        <section className={styles.process}>
          <h2>How It Works</h2>
          <div className={styles.steps}>
            <div className={styles.step}>
              <div className={styles.stepNumber}>1</div>
              <h3>Contact Us</h3>
              <p>Send an email describing your project and which service you're interested in.</p>
            </div>
            <div className={styles.step}>
              <div className={styles.stepNumber}>2</div>
              <h3>Initial Discussion</h3>
              <p>We'll schedule a brief (free) call to understand your needs and confirm fit.</p>
            </div>
            <div className={styles.step}>
              <div className={styles.stepNumber}>3</div>
              <h3>Engagement</h3>
              <p>Sign agreement, pay deposit, and we get started helping you build your dream home.</p>
            </div>
          </div>
        </section>

        <section className={styles.cta}>
          <h2>Ready to Get Expert Guidance?</h2>
          <p>
            Have questions about which service is right for you? Send us an email and let's discuss
            your project.
          </p>
          <a href="mailto:consulting@build-your-house.com?subject=Consulting Inquiry" className={styles.ctaButton}>
            Contact Us Today
          </a>
        </section>
      </div>
    </div>
  );
}
