import MaterialEstimatorCalculator from '@/components/MaterialEstimatorCalculator';
import type { Metadata } from 'next';
import styles from '../../feasibility/cost-savings-calculator/calculator-page.module.css';

export const metadata: Metadata = {
  title: "Free Construction Material Calculator — Estimate Lumber, Concrete & Roofing",
  description: "Calculate exactly how much lumber, concrete, roofing, and siding you need for your build. Free material estimator with cost breakdowns. Save thousands on materials.",
};

export default function MaterialEstimatorPage() {
  return (
    <div className={styles.page}>
      <div className={styles.container}>
        <header className={styles.header}>
          <h1>Material Estimator Calculator</h1>
          <p className={styles.subtitle}>
            Get accurate estimates for the major materials you'll need to build your home.
            This calculator provides realistic quantities and costs based on your project specifications,
            helping you budget and plan your material orders.
          </p>
        </header>

        <MaterialEstimatorCalculator />

        <section className={styles.info}>
          <h2>Understanding Material Estimates</h2>

          <div className={styles.infoGrid}>
            <div className={styles.infoCard}>
              <h3>Concrete & Foundation</h3>
              <p>
                Foundation concrete includes the slab (typically 4 inches thick) and footings.
                Concrete is measured in cubic yards and costs vary by region, typically $120-$180 per yard delivered.
              </p>
              <p>
                <strong>Important:</strong> This estimate doesn't include rebar, vapor barrier, or
                insulation under the slab. Budget an additional 15-20% for these items.
              </p>
            </div>

            <div className={styles.infoCard}>
              <h3>Framing Lumber</h3>
              <p>
                Framing lumber includes studs (2x4 or 2x6), floor joists, roof rafters/trusses, headers,
                and sheathing. Lumber is measured in board feet (bf) and prices fluctuate significantly.
              </p>
              <p>
                <strong>Pro tip:</strong> Lumber prices can swing 50-100% based on market conditions.
                Get current quotes from multiple suppliers and consider locking in prices if favorable.
              </p>
            </div>

            <div className={styles.infoCard}>
              <h3>Drywall</h3>
              <p>
                Standard drywall sheets are 4x8 feet (32 square feet). This estimate includes interior
                walls and all ceilings. Don't forget to budget for joint compound, tape, and corner bead.
              </p>
              <p>
                <strong>Finish level matters:</strong> Basic finish uses standard 1/2" drywall.
                Premium uses 5/8" drywall on ceilings and may include moisture-resistant or soundproofing options.
              </p>
            </div>

            <div className={styles.infoCard}>
              <h3>Roofing</h3>
              <p>
                Roofing is measured in "squares" (100 square feet). This estimate includes shingles and
                underlayment. Roof complexity significantly affects material needs due to waste from cuts and valleys.
              </p>
              <p>
                <strong>Don't forget:</strong> Ridge vent, drip edge, flashing, and ice/water shield
                add 15-25% to shingle costs. Factor these in your total roofing budget.
              </p>
            </div>

            <div className={styles.infoCard}>
              <h3>Flooring</h3>
              <p>
                Flooring estimates are based on finished square footage. Basic includes laminate or
                basic vinyl, standard includes mid-grade hardwood or tile, premium includes high-end
                hardwood or natural stone.
              </p>
              <p>
                <strong>Installation:</strong> These are material costs only. Professional installation
                typically adds $2-8 per square foot depending on material complexity.
              </p>
            </div>

            <div className={styles.infoCard}>
              <h3>Insulation</h3>
              <p>
                Insulation covers exterior walls and ceiling areas. Costs vary by R-value and type
                (fiberglass batts, blown-in, or spray foam). Higher finish levels assume better R-values.
              </p>
              <p>
                <strong>Energy savings:</strong> Don't cheap out on insulation. The payback in energy
                savings is typically 3-7 years, and it significantly impacts comfort.
              </p>
            </div>
          </div>
        </section>

        <section className={styles.reality}>
          <h2>What's NOT Included</h2>
          <p>
            This calculator estimates major structural materials. Your total material budget needs
            to include many additional items:
          </p>

          <div className={styles.considerations}>
            <div className={styles.consideration}>
              <h4>Windows & Doors</h4>
              <p>
                Exterior doors, interior doors, windows, and hardware can easily add $15,000-$40,000
                to your budget depending on quantity and quality.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>MEP Systems</h4>
              <p>
                Mechanical (HVAC), Electrical, and Plumbing systems including equipment, fixtures,
                wire, pipe, and ductwork typically cost $30,000-$60,000 for a typical home.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Cabinets & Countertops</h4>
              <p>
                Kitchen and bathroom cabinets, countertops, and vanities vary wildly in price.
                Budget $8,000-$30,000 for a typical kitchen.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Appliances & Fixtures</h4>
              <p>
                Appliances, light fixtures, plumbing fixtures (toilets, sinks, faucets), and finish
                hardware add up quickly. Plan for $15,000-$35,000.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Exterior Finishes</h4>
              <p>
                Siding, trim, paint, gutters, and soffit/fascia. Costs vary dramatically by material
                choice. Budget $8,000-$25,000 depending on home size and finishes.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Site Work</h4>
              <p>
                Excavation, grading, driveway, utilities connections, and landscaping. These
                site-specific costs often surprise first-time builders. Budget $15,000-$40,000.
              </p>
            </div>
          </div>
        </section>

        <section className={styles.reality} style={{ backgroundColor: 'var(--color-bg-light)', marginTop: '3rem' }}>
          <h2>Material Ordering Tips</h2>
          <p>Based on 15+ years of GC experience, here's what you need to know:</p>

          <div className={styles.considerations}>
            <div className={styles.consideration}>
              <h4>Order 10% Extra</h4>
              <p>
                Always order 10-15% extra for waste, cuts, mistakes, and future repairs.
                This is especially important for items that may be discontinued (flooring, tile, siding).
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Get Contractor Accounts</h4>
              <p>
                Set up accounts at lumber yards and suppliers. You'll get better pricing (10-20% off retail),
                delivery options, and access to contractor-grade materials.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Time Your Orders</h4>
              <p>
                Don't buy everything up front. Order materials 1-2 weeks before you need them to avoid
                theft, weather damage, and tying up cash. Exception: lock in lumber if prices are favorable.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Inspect Deliveries</h4>
              <p>
                Check every delivery before signing. Look for damaged materials, incorrect quantities,
                and wrong items. It's much harder to get credit after the driver leaves.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Store Materials Properly</h4>
              <p>
                Protect materials from weather. Wet lumber warps, wet drywall is ruined, and
                moisture-damaged materials cause long-term problems. Use tarps and keep materials elevated.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Track Everything</h4>
              <p>
                Keep all receipts and track every material purchase. This helps with budget tracking,
                warranty claims, and provides documentation for building inspectors if needed.
              </p>
            </div>
          </div>
        </section>

        <section className={styles.nextSteps}>
          <h2>Next Steps</h2>
          <p>Now that you have a material estimate, continue planning your owner-builder project.</p>
          <div className={styles.ctaButtons}>
            <a href="/calculators/timeline-estimator" className={styles.primaryButton}>
              Estimate Your Timeline
            </a>
            <a href="/calculators/budget-tracker" className={styles.secondaryButton}>
              Track Your Budget
            </a>
          </div>
        </section>
      </div>
    </div>
  );
}
