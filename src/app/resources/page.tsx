import Section from '@/components/Section';
import CalloutBox from '@/components/CalloutBox';
import Link from 'next/link';

export default function ResourcesPage() {
  return (
    <div className="content-container">
      <h1>Owner-Builder Resources</h1>

      <p>
        Essential tools, templates, and resources to help you successfully
        build your own home. Everything here is free and based on 15+ years
        of general contracting experience.
      </p>

      <Section title="Free Downloads">
        <div className="resource-grid">
          {/* Checklists Card */}
          <Link href="/resources/checklists" className="resource-card">
            <div className="resource-icon">📋</div>
            <h3>Checklists</h3>
            <p>
              Comprehensive checklists for every phase from permitting
              through final inspection. Never miss a critical step.
            </p>
            <div className="resource-link">View Checklists →</div>
          </Link>

          {/* Templates Card */}
          <Link href="/resources/templates" className="resource-card">
            <div className="resource-icon">📄</div>
            <h3>Templates</h3>
            <p>
              Contractor agreements, change orders, payment schedules,
              and inspection forms ready to customize.
            </p>
            <div className="resource-link">Download Templates →</div>
          </Link>

          {/* Glossary Card */}
          <Link href="/resources/glossary" className="resource-card">
            <div className="resource-icon">📖</div>
            <h3>Construction Glossary</h3>
            <p>
              Understand construction terminology. Know what contractors
              and inspectors are talking about.
            </p>
            <div className="resource-link">Browse Glossary →</div>
          </Link>
        </div>
      </Section>

      <Section title="Calculators & Tools">
        <p>
          Use these free calculators to estimate costs, plan timelines,
          and track your budget throughout the build process.
        </p>

        <div className="resource-grid">
          {/* Calculator cards */}
          <Link href="/calculators/material-estimator" className="resource-card">
            <div className="resource-icon">🧮</div>
            <h3>Material Estimator</h3>
            <p>Calculate quantities and costs for major materials</p>
            <div className="resource-link">Use Calculator →</div>
          </Link>

          <Link href="/feasibility/cost-savings-calculator" className="resource-card">
            <div className="resource-icon">💰</div>
            <h3>Cost Savings Calculator</h3>
            <p>See how much you can save as an owner-builder</p>
            <div className="resource-link">Calculate Savings →</div>
          </Link>

          <Link href="/calculators/timeline-estimator" className="resource-card">
            <div className="resource-icon">📅</div>
            <h3>Timeline Estimator</h3>
            <p>Plan your build schedule and time commitment</p>
            <div className="resource-link">Estimate Timeline →</div>
          </Link>

          <Link href="/calculators/budget-tracker" className="resource-card">
            <div className="resource-icon">📊</div>
            <h3>Budget Tracker</h3>
            <p>Track expenses and stay on budget</p>
            <div className="resource-link">Track Budget →</div>
          </Link>
        </div>
      </Section>

      <Section title="Recommended Reading" variant="highlighted">
        <CalloutBox type="info">
          <strong>Code Books & References</strong>
          <ul>
            <li>International Residential Code (IRC) - Your bible for residential construction</li>
            <li>NEC (National Electrical Code) - Required for electrical work</li>
            <li>Local building code amendments - Check with your building department</li>
          </ul>
        </CalloutBox>

        <CalloutBox type="tip" title="Pro Tip">
          Many building departments offer free code books or have copies
          available for reference. Ask during your pre-application meeting.
        </CalloutBox>
      </Section>

      <Section title="External Resources">
        <p>
          While we provide comprehensive guidance, these external resources
          can supplement your knowledge:
        </p>

        <h3>Government Resources</h3>
        <ul>
          <li><strong>ICC (International Code Council)</strong> - Building codes and standards</li>
          <li><strong>OSHA</strong> - Safety requirements and best practices</li>
          <li><strong>EPA</strong> - Environmental regulations and lead paint rules</li>
        </ul>

        <h3>Industry Organizations</h3>
        <ul>
          <li><strong>NAHB (National Association of Home Builders)</strong> - Industry standards</li>
          <li><strong>AIA (American Institute of Architects)</strong> - Design resources</li>
        </ul>

        <CalloutBox type="warning">
          Always verify that external information applies to YOUR jurisdiction.
          Building codes vary by state and locality.
        </CalloutBox>
      </Section>
    </div>
  );
}
