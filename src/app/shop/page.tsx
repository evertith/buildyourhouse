import Section from '@/components/Section';
import CalloutBox from '@/components/CalloutBox';

export const metadata = {
  title: 'Owner-Builder Job Site Binder — 229 Pages of Templates & Checklists',
  description: 'The complete owner-builder toolkit: 229 pages of contracts, checklists, inspection forms, and budget trackers. Print it, take it to the job site. $97 instant download.',
  keywords: 'owner builder templates, construction checklists, job site binder, building contracts, owner builder tools',
};

export default function JobSiteBinder() {
  return (
    <div className="content-container">
      {/* Hero Section */}
      <div className="hero-section" style={{
        textAlign: 'center',
        padding: 'var(--space-16) 0',
        backgroundColor: 'var(--surface-warm)'
      }}>
        <div style={{ maxWidth: '800px', margin: '0 auto' }}>
          <h1 style={{
            fontSize: 'var(--text-4xl)',
            marginBottom: 'var(--space-4)',
            lineHeight: 'var(--leading-tight)'
          }}>
            Stop Fumbling With Your Phone on the Job Site
          </h1>

          <p style={{
            fontSize: 'var(--text-xl)',
            color: 'var(--text-secondary)',
            marginBottom: 'var(--space-8)',
            lineHeight: 'var(--leading-relaxed)'
          }}>
            The Complete Owner-Builder Job Site Binder System — Everything you need
            to manage your build, printed and organized in one place.
          </p>

          <div style={{
            display: 'flex',
            gap: 'var(--space-4)',
            justifyContent: 'center',
            alignItems: 'center',
            marginBottom: 'var(--space-6)',
            flexWrap: 'wrap'
          }}>
            <div className="stat-badge">
              <strong>229 pages</strong> of templates & checklists
            </div>
            <div className="stat-badge">
              <strong>Instant download</strong> — start printing today
            </div>
            <div className="stat-badge">
              <strong>One-time payment</strong> — lifetime access
            </div>
          </div>

          <a href="#purchase" className="button button-large" style={{
            fontSize: 'var(--text-xl)',
            padding: 'var(--space-6) var(--space-12)'
          }}>
            Get the Complete System — $97
          </a>

          <p style={{
            marginTop: 'var(--space-4)',
            fontSize: 'var(--text-sm)',
            color: 'var(--text-secondary)'
          }}>
            30-day money-back guarantee • Instant digital download
          </p>
        </div>
      </div>

      {/* Problem/Agitation Section */}
      <Section
        title="The Problem Every Owner-Builder Faces"
        spacing="large"
      >
        <div className="problem-grid">
          <div className="problem-card">
            <div className="problem-icon">📱</div>
            <h3>Phone Fumbling</h3>
            <p>
              Ever tried pulling up a PDF on your phone with muddy gloves?
              Or scrolling through documents while an inspector waits?
            </p>
          </div>

          <div className="problem-card">
            <div className="problem-icon">📶</div>
            <h3>No Signal</h3>
            <p>
              Lost cell service right when you need that electrical diagram?
              Dead zones on construction sites are common.
            </p>
          </div>

          <div className="problem-card">
            <div className="problem-icon">🔋</div>
            <h3>Dead Battery</h3>
            <p>
              Your phone died at the worst possible moment? Now you can&apos;t
              access contracts, checklists, or critical information.
            </p>
          </div>

          <div className="problem-card">
            <div className="problem-icon">🤝</div>
            <h3>Hard to Share</h3>
            <p>
              Ever tried showing a subcontractor a contract on a 6-inch screen?
              Or emailing documents back and forth on site?
            </p>
          </div>

          <div className="problem-card">
            <div className="problem-icon">📋</div>
            <h3>Disorganized Chaos</h3>
            <p>
              Spreadsheets on your laptop, PDFs in email, notes on your phone.
              Nothing is where you need it when you need it.
            </p>
          </div>

          <div className="problem-card">
            <div className="problem-icon">⏰</div>
            <h3>Wasted Time</h3>
            <p>
              Searching through files, re-downloading documents, remembering
              what you forgot to check. Hours lost to disorganization.
            </p>
          </div>
        </div>

        <div style={{
          textAlign: 'center',
          marginTop: 'var(--space-12)',
          padding: 'var(--space-8)',
          backgroundColor: 'var(--critical-bg)',
          borderRadius: 'var(--radius-lg)',
          borderLeft: '4px solid var(--danger)'
        }}>
          <h3 style={{ marginTop: 0, fontSize: 'var(--text-2xl)' }}>
            There&apos;s a Better Way
          </h3>
          <p style={{
            fontSize: 'var(--text-lg)',
            marginBottom: 0
          }}>
            Don&apos;t rely on your phone. Use organized
            binders with everything you need at your fingertips.
          </p>
        </div>
      </Section>

      {/* Solution Section */}
      <Section
        title="The Job Site Binder Puts Everything In Your Hands"
        background="warm"
        spacing="large"
      >
        <div className="benefits-grid">
          <div className="benefit-item">
            <span className="benefit-icon">✅</span>
            <div>
              <h4>No Internet Required</h4>
              <p>Everything printed and accessible, even in dead zones</p>
            </div>
          </div>

          <div className="benefit-item">
            <span className="benefit-icon">✅</span>
            <div>
              <h4>Easy to Share</h4>
              <p>Hand subs and inspectors the exact page they need</p>
            </div>
          </div>

          <div className="benefit-item">
            <span className="benefit-icon">✅</span>
            <div>
              <h4>Professional Appearance</h4>
              <p>Show up organized and earn instant credibility</p>
            </div>
          </div>

          <div className="benefit-item">
            <span className="benefit-icon">✅</span>
            <div>
              <h4>Durable & Weather-Resistant</h4>
              <p>Binders survive job sites better than phones</p>
            </div>
          </div>

          <div className="benefit-item">
            <span className="benefit-icon">✅</span>
            <div>
              <h4>Write Notes Directly</h4>
              <p>Mark up documents, add notes, track changes on paper</p>
            </div>
          </div>

          <div className="benefit-item">
            <span className="benefit-icon">✅</span>
            <div>
              <h4>Never Lose Information</h4>
              <p>Physical backup that doesn&apos;t depend on batteries or cloud storage</p>
            </div>
          </div>
        </div>
      </Section>

      {/* What's Inside Section */}
      <Section
        title="What's Inside the Complete System"
        subtitle="229 pages of templates, checklists, forms, and spreadsheets"
        spacing="large"
      >
        <div className="whats-inside-grid">
          {/* Section 1 */}
          <div className="inside-card">
            <div className="inside-header">
              <span className="inside-number">01</span>
              <h3>Project Planning</h3>
            </div>
            <ul>
              <li>Project Overview Template</li>
              <li>Budget Master Spreadsheet (Excel + PDF)</li>
              <li>Timeline Planner (printable Gantt chart)</li>
              <li>Contact List Template</li>
              <li>Material Order Tracking Sheets</li>
              <li>Permit Application Checklist</li>
            </ul>
          </div>

          {/* Section 2 */}
          <div className="inside-card">
            <div className="inside-header">
              <span className="inside-number">02</span>
              <h3>Contract Templates</h3>
            </div>
            <ul>
              <li>General Subcontractor Agreement (editable Word doc)</li>
              <li>Scope of Work Template</li>
              <li>Change Order Form</li>
              <li>Payment Schedule Template</li>
              <li>Lien Waiver Forms</li>
              <li>Insurance Certificate Request Letter</li>
            </ul>
          </div>

          {/* Section 3 */}
          <div className="inside-card">
            <div className="inside-header">
              <span className="inside-number">03</span>
              <h3>Phase Checklists</h3>
            </div>
            <ul>
              <li>Permit Application (20+ items)</li>
              <li>Foundation Phase (30+ items)</li>
              <li>Framing Phase (40+ items)</li>
              <li>Rough-In by Trade (Electrical, Plumbing, HVAC)</li>
              <li>Insulation & Drywall</li>
              <li>Finish Work</li>
              <li>Final Inspection Prep</li>
            </ul>
          </div>

          {/* Section 4 */}
          <div className="inside-card">
            <div className="inside-header">
              <span className="inside-number">04</span>
              <h3>Inspection Prep Sheets</h3>
            </div>
            <ul>
              <li>Footing Inspection Prep</li>
              <li>Foundation Inspection Prep</li>
              <li>Framing Inspection Prep</li>
              <li>Rough-In Inspection Prep (by trade)</li>
              <li>Insulation Inspection Prep</li>
              <li>Final Inspection Prep</li>
              <li>Common Inspection Failures & Fixes</li>
            </ul>
          </div>

          {/* Section 5 */}
          <div className="inside-card">
            <div className="inside-header">
              <span className="inside-number">05</span>
              <h3>Daily Management</h3>
            </div>
            <ul>
              <li>Daily Site Log Template</li>
              <li>Subcontractor Sign-In Sheet</li>
              <li>Material Delivery Log</li>
              <li>Weather Delay Tracker</li>
              <li>Problem/Issue Tracking Form</li>
              <li>Photo Documentation Log</li>
            </ul>
          </div>

          {/* Section 6 */}
          <div className="inside-card">
            <div className="inside-header">
              <span className="inside-number">06</span>
              <h3>Budget & Expense Tracking</h3>
            </div>
            <ul>
              <li>Master Budget Spreadsheet (auto-calculating Excel)</li>
              <li>Expense Tracking by Category</li>
              <li>Payment Log Template</li>
              <li>Receipt Organization System</li>
              <li>Cost Overrun Alert Worksheet</li>
            </ul>
          </div>

          {/* Section 7 */}
          <div className="inside-card">
            <div className="inside-header">
              <span className="inside-number">07</span>
              <h3>Subcontractor Management</h3>
            </div>
            <ul>
              <li>Subcontractor Interview Scorecard</li>
              <li>Reference Check Form</li>
              <li>Performance Review Template</li>
              <li>Payment Request Form</li>
              <li>Punch List Template</li>
            </ul>
          </div>

          {/* Section 8 */}
          <div className="inside-card">
            <div className="inside-header">
              <span className="inside-number">08</span>
              <h3>Quick Reference Guides</h3>
            </div>
            <ul>
              <li>Building Code Quick Reference (IRC highlights)</li>
              <li>Lumber Span Tables</li>
              <li>Nail Schedule Chart</li>
              <li>Common Measurement Conversions</li>
              <li>Concrete Mixing Ratios</li>
              <li>Wire Gauge & Ampacity Chart</li>
            </ul>
          </div>
        </div>

        <CalloutBox type="success" title="🎁 BONUS: Digital Tools Included">
          <strong>You also get digital versions for backup:</strong>
          <ul style={{ marginBottom: 0, marginTop: 'var(--space-3)' }}>
            <li>Calculator Spreadsheets (Material estimator, Timeline planner)</li>
            <li>Google Sheets Templates (cloud backup versions)</li>
            <li>QR codes linking to online resources</li>
          </ul>
        </CalloutBox>
      </Section>

      {/* Social Proof Section */}
      <Section background="warm" spacing="large">
        <div className="testimonial-card">
          <div className="testimonial-content">
            <div className="quote-mark">&ldquo;</div>
            <p style={{ fontSize: 'var(--text-lg)', fontStyle: 'italic' }}>
              I printed the entire binder before breaking ground. Having everything
              organized and accessible made me look like I knew what I was doing —
              even when I didn&apos;t. The inspector even commented on how prepared I was.
            </p>
            <div className="testimonial-author">
              <strong>Mike T.</strong>
              <span>Built 2,400 sq ft home in Texas</span>
            </div>
          </div>
        </div>

        <div className="testimonial-card">
          <div className="testimonial-content">
            <div className="quote-mark">&ldquo;</div>
            <p style={{ fontSize: 'var(--text-lg)', fontStyle: 'italic' }}>
              Best $97 I spent on the entire build. The contract templates alone
              saved me a ton of time. The checklists kept me on track through
              every phase.
            </p>
            <div className="testimonial-author">
              <strong>Jennifer L.</strong>
              <span>Built 1,800 sq ft home in North Carolina</span>
            </div>
          </div>
        </div>
      </Section>

      {/* How It Works Section */}
      <Section title="How It Works" spacing="large">
        <div className="how-it-works-grid">
          <div className="step-card">
            <div className="step-number">1</div>
            <h3>Purchase & Download</h3>
            <p>
              Instant access to the complete ZIP file with all 229 pages
              of templates, checklists, and forms.
            </p>
          </div>

          <div className="step-card">
            <div className="step-number">2</div>
            <h3>Print & Organize</h3>
            <p>
              Follow the included &ldquo;START HERE&rdquo; guide to print and assemble
              your binder. Takes about 2 hours.
            </p>
          </div>

          <div className="step-card">
            <div className="step-number">3</div>
            <h3>Take to Job Site</h3>
            <p>
              Show up organized and professional. Everything you need at
              your fingertips — no phone required.
            </p>
          </div>

          <div className="step-card">
            <div className="step-number">4</div>
            <h3>Build With Confidence</h3>
            <p>
              Use the checklists, templates, and forms throughout your build.
              Never miss a critical step again.
            </p>
          </div>
        </div>

        <CalloutBox type="info">
          <strong>Printing Cost Estimate:</strong> Expect to spend $40-60 at an
          office supply store for printing and binding. Print double-sided to
          save paper and money.
        </CalloutBox>
      </Section>

      {/* Purchase Section */}
      <Section
        title="Get The Complete System Today"
        spacing="large"
        background="warm"
      >
        <div id="purchase" className="purchase-box">
          <div className="purchase-content">
            <h2 style={{ marginTop: 0 }}>
              The Complete Owner-Builder Job Site Binder System
            </h2>

            <div className="purchase-includes">
              <h3>What You Get:</h3>
              <ul>
                <li>✅ 229 pages of templates, checklists, and forms</li>
                <li>✅ 8 comprehensive sections covering every phase</li>
                <li>✅ Editable Word & Excel files for customization</li>
                <li>✅ Printable PDFs optimized for 3-ring binders</li>
                <li>✅ Digital backup tools (spreadsheets & calculators)</li>
                <li>✅ &ldquo;START HERE&rdquo; binder assembly guide</li>
                <li>✅ Lifetime access to all files</li>
                <li>✅ Free updates when we add new content</li>
              </ul>
            </div>

            <div className="purchase-price">
              <div className="price-tag">
                <span className="price-label">One-Time Payment</span>
                <span className="price-amount">$97</span>
                <span className="price-subtext">Instant digital download</span>
              </div>
            </div>

            {/* Stripe Payment Link */}
            <div className="purchase-button-container">
              <a
                href="https://buy.stripe.com/5kQ28racn54z0ReeZ5fAc00"
                className="button button-large"
                style={{
                  fontSize: 'var(--text-xl)',
                  padding: 'var(--space-6) var(--space-12)',
                  width: '100%',
                  maxWidth: '500px',
                  textAlign: 'center'
                }}
              >
                Get Instant Access — $97
              </a>
            </div>

            <div className="purchase-guarantees">
              <div className="guarantee-item">
                <span style={{ fontSize: 'var(--text-2xl)' }}>🔒</span>
                <div>
                  <strong>Secure Checkout</strong>
                  <p>Powered by Stripe - your payment info is safe</p>
                </div>
              </div>

              <div className="guarantee-item">
                <span style={{ fontSize: 'var(--text-2xl)' }}>⚡</span>
                <div>
                  <strong>Instant Access</strong>
                  <p>Download immediately after purchase</p>
                </div>
              </div>

              <div className="guarantee-item">
                <span style={{ fontSize: 'var(--text-2xl)' }}>✅</span>
                <div>
                  <strong>30-Day Guarantee</strong>
                  <p>If it doesn&apos;t save you 10+ hours, get a full refund</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <CalloutBox type="success" title="🎯 Money-Back Guarantee">
          If the Job Site Binder doesn&apos;t save you at least 10 hours of frustration
          and keep you organized throughout your build, just email us within 30 days
          for a full refund. No questions asked.
        </CalloutBox>
      </Section>

      {/* FAQ Section */}
      <Section title="Frequently Asked Questions" spacing="large">
        <div className="faq-list">
          <div className="faq-item">
            <h3>Do I need special equipment to print this?</h3>
            <p>
              No. Any standard printer works. You can print at home or take the
              PDF files to an office supply store (Staples, Office Depot, FedEx
              Office). Expect to spend $40-60 for printing and binding.
            </p>
          </div>

          <div className="faq-item">
            <h3>Can I customize the templates?</h3>
            <p>
              Yes! Contract templates and tracking sheets come as editable Word
              and Excel files. Customize them with your project details, add your
              logo, or modify to fit your needs.
            </p>
          </div>

          <div className="faq-item">
            <h3>Is this legal in my state?</h3>
            <p>
              The templates are general-purpose construction documents used
              nationwide. However, always verify contracts with a local attorney
              and ensure compliance with your state&apos;s building codes and regulations.
            </p>
          </div>

          <div className="faq-item">
            <h3>Do you offer updates?</h3>
            <p>
              Yes! When we add new templates or update existing ones, you&apos;ll get
              free access to download the latest version. Your purchase includes
              lifetime access to all updates.
            </p>
          </div>

          <div className="faq-item">
            <h3>What if I have questions while using the binder?</h3>
            <p>
              Browse our free guides on Build Your House for detailed explanations
              of each construction phase. The website has hundreds of pages of
              owner-builder advice to complement the binder system.
            </p>
          </div>

          <div className="faq-item">
            <h3>Can I share this with my spouse or partner?</h3>
            <p>
              Absolutely! Use it for your personal owner-builder project. Please
              don&apos;t distribute or resell the files, but printing multiple copies
              for your own build is perfectly fine.
            </p>
          </div>

          <div className="faq-item">
            <h3>What format are the files in?</h3>
            <p>
              PDFs for printing, Word docs (.docx) for contracts and letters,
              Excel spreadsheets (.xlsx) for budgets and calculators. Everything
              works on Windows and Mac.
            </p>
          </div>

          <div className="faq-item">
            <h3>How soon can I download this?</h3>
            <p>
              Immediately after purchase. You&apos;ll receive an email with download
              links within minutes. No waiting, no shipping — instant access to
              all files.
            </p>
          </div>
        </div>
      </Section>

      {/* Final CTA Section */}
      <Section spacing="large" background="warm">
        <div style={{ textAlign: 'center', maxWidth: '700px', margin: '0 auto' }}>
          <h2 style={{ fontSize: 'var(--text-3xl)' }}>
            Stop Wasting Time Searching for Information
          </h2>
          <p style={{ fontSize: 'var(--text-lg)', color: 'var(--text-secondary)' }}>
            Get organized, look professional, and build with confidence.
            Everything you need in one comprehensive binder system.
          </p>

          <div style={{ marginTop: 'var(--space-8)' }}>
            <a
              href="#purchase"
              className="button button-large"
              style={{
                fontSize: 'var(--text-xl)',
                padding: 'var(--space-6) var(--space-12)'
              }}
            >
              Get the Complete System — $97
            </a>
          </div>

          <p style={{
            marginTop: 'var(--space-4)',
            fontSize: 'var(--text-sm)',
            color: 'var(--text-secondary)'
          }}>
            30-day money-back guarantee • Instant download • Lifetime access
          </p>
        </div>
      </Section>
    </div>
  );
}
