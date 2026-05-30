'use client';

import { useState } from 'react';
import { calculateCostSavings, CostSavingsInputs, CostSavingsResults } from '@/lib/calculators';
import CalculatorCard from '@/components/CalculatorCard';
import styles from '@/styles/Calculator.module.css';

export default function CostSavingsCalculator() {
  const [inputs, setInputs] = useState<CostSavingsInputs>({
    homeSize: 2000,
    estimatedCost: 300000,
    gcFeePercentage: 14,
    laborHours: 500,
    hourlyWage: 30
  });

  const [results, setResults] = useState<CostSavingsResults | null>(null);

  const handleInputChange = (field: keyof CostSavingsInputs, value: number) => {
    setInputs(prev => ({ ...prev, [field]: value }));
  };

  const calculate = () => {
    const calculatedResults = calculateCostSavings(inputs);
    setResults(calculatedResults);
  };

  const formatCurrency = (value: number) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      maximumFractionDigits: 0
    }).format(value);
  };

  return (
    <CalculatorCard
      title="Cost Savings Calculator"
      description="Calculate how much money you can save by being your own general contractor"
    >
      <div className={styles.calculator}>
        <div className={styles.inputs}>
          <h3 className={styles.sectionTitle}>Your Project Details</h3>

        <div className={styles.inputGroup}>
          <label htmlFor="homeSize">Home Size (square feet)</label>
          <input
            id="homeSize"
            type="number"
            value={inputs.homeSize}
            onChange={(e) => handleInputChange('homeSize', Number(e.target.value))}
            min="500"
            max="10000"
            step="100"
          />
        </div>

        <div className={styles.inputGroup}>
          <label htmlFor="estimatedCost">Estimated Total Construction Cost</label>
          <input
            id="estimatedCost"
            type="number"
            value={inputs.estimatedCost}
            onChange={(e) => handleInputChange('estimatedCost', Number(e.target.value))}
            min="50000"
            max="2000000"
            step="10000"
          />
          <span className={styles.hint}>Include materials and subcontractor labor</span>
        </div>

        <div className={styles.inputGroup}>
          <label htmlFor="gcFeePercentage">Typical GC Fee in Your Area (%)</label>
          <input
            id="gcFeePercentage"
            type="number"
            value={inputs.gcFeePercentage}
            onChange={(e) => handleInputChange('gcFeePercentage', Number(e.target.value))}
            min="10"
            max="30"
            step="1"
          />
          <span className={styles.hint}>Usually 15-20%, higher in competitive markets</span>
        </div>

        <div className={styles.inputGroup}>
          <label htmlFor="laborHours">Hours You'll Work Yourself</label>
          <input
            id="laborHours"
            type="number"
            value={inputs.laborHours}
            onChange={(e) => handleInputChange('laborHours', Number(e.target.value))}
            min="0"
            max="3000"
            step="50"
          />
          <span className={styles.hint}>Typical owner-builder: 400-1000 hours</span>
        </div>

        <div className={styles.inputGroup}>
          <label htmlFor="hourlyWage">Value of Your Time ($/hour)</label>
          <input
            id="hourlyWage"
            type="number"
            value={inputs.hourlyWage}
            onChange={(e) => handleInputChange('hourlyWage', Number(e.target.value))}
            min="0"
            max="200"
            step="5"
          />
          <span className={styles.hint}>What you'd earn working elsewhere, or value of free time</span>
        </div>

        <button onClick={calculate} className={styles.calculateButton}>
          Calculate My Savings
        </button>
      </div>

      {results && (
        <div className={styles.results}>
          <h3 className={styles.sectionTitle}>Your Potential Savings</h3>

          <div className={styles.resultCard + ' ' + styles.highlight}>
            <div className={styles.resultLabel}>Total Cash Savings</div>
            <div className={styles.resultValue}>{formatCurrency(results.totalSavings)}</div>
            <div className={styles.resultDetail}>
              {results.percentageSaved.toFixed(1)}% of construction cost — the GC fee you avoid
            </div>
          </div>

          <div className={styles.resultCard}>
            <div className={styles.resultLabel}>GC Fee Savings</div>
            <div className={styles.resultValue}>{formatCurrency(results.gcFeeSavings)}</div>
            <div className={styles.resultDetail}>
              Money you save by managing the project yourself
            </div>
          </div>

          <div className={styles.resultCard}>
            <div className={styles.resultLabel}>Imputed Value of Your Time (not cash savings)</div>
            <div className={styles.resultValue}>{formatCurrency(results.laborValueSavings)}</div>
            <div className={styles.resultDetail}>
              Value of {inputs.laborHours} hours at ${inputs.hourlyWage}/hour. This is the worth of
              your own labor — it is not added to your cash savings above.
            </div>
          </div>

          <div className={styles.disclaimer}>
            Estimate only — not financial advice. Actual savings vary, and owner-building
            carries additional costs and risks (insurance, permits, financing, re-work).
          </div>

          <div className={styles.breakdown}>
            <h4>What This Means</h4>
            <ul>
              <li>
                <strong>Net Project Cost:</strong> {formatCurrency(inputs.estimatedCost - results.gcFeeSavings)}
                <br />
                <span className={styles.comparison}>vs. {formatCurrency(inputs.estimatedCost)} with a GC</span>
              </li>
              <li>
                <strong>Your Time Investment:</strong> {inputs.laborHours} hours ({(inputs.laborHours / 40).toFixed(0)} weeks at 40 hrs/week)
              </li>
              <li>
                <strong>Cash Savings:</strong> You pocket {formatCurrency(results.gcFeeSavings)} by
                avoiding the GC fee. Your {formatCurrency(results.laborValueSavings)} of labor is
                sweat equity you contribute, not cash you save.
              </li>
            </ul>
          </div>

          <div className={styles.cta}>
            <p>Ready to learn how to capture these savings?</p>
            <a href="/start-here" className={styles.ctaButton}>
              See the Complete Roadmap
            </a>
          </div>
        </div>
      )}
      </div>
    </CalculatorCard>
  );
}
