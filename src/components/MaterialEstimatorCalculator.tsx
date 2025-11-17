'use client';

import { useState } from 'react';
import { calculateMaterialEstimate, MaterialEstimatorInputs, MaterialEstimatorResults } from '@/lib/calculators';
import CalculatorCard from '@/components/CalculatorCard';
import styles from '@/styles/Calculator.module.css';

export default function MaterialEstimatorCalculator() {
  const [inputs, setInputs] = useState<MaterialEstimatorInputs>({
    homeSize: 2000,
    stories: 1,
    roofComplexity: 'moderate',
    wallHeight: 8,
    finishLevel: 'standard'
  });

  const [results, setResults] = useState<MaterialEstimatorResults | null>(null);

  const handleInputChange = (field: keyof MaterialEstimatorInputs, value: number | string) => {
    setInputs(prev => ({ ...prev, [field]: value }));
  };

  const calculate = () => {
    const calculatedResults = calculateMaterialEstimate(inputs);
    setResults(calculatedResults);
  };

  const formatCurrency = (value: number) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      maximumFractionDigits: 0
    }).format(value);
  };

  const formatNumber = (value: number) => {
    return new Intl.NumberFormat('en-US', {
      maximumFractionDigits: 1
    }).format(value);
  };

  return (
    <CalculatorCard
      title="Material Estimator"
      description="Calculate material quantities and costs for your home build project"
    >
      <div className={styles.calculator}>
        <div className={styles.inputs}>
          <h3 className={styles.sectionTitle}>Project Specifications</h3>

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
          <span className={styles.hint}>Total finished square footage</span>
        </div>

        <div className={styles.inputGroup}>
          <label htmlFor="stories">Number of Stories</label>
          <select
            id="stories"
            value={inputs.stories}
            onChange={(e) => handleInputChange('stories', Number(e.target.value))}
          >
            <option value={1}>1 Story</option>
            <option value={2}>2 Stories</option>
            <option value={3}>3 Stories</option>
          </select>
        </div>

        <div className={styles.inputGroup}>
          <label htmlFor="roofComplexity">Roof Complexity</label>
          <select
            id="roofComplexity"
            value={inputs.roofComplexity}
            onChange={(e) => handleInputChange('roofComplexity', e.target.value)}
          >
            <option value="simple">Simple (Gable)</option>
            <option value="moderate">Moderate (Hip/Mixed)</option>
            <option value="complex">Complex (Multiple Valleys)</option>
          </select>
          <span className={styles.hint}>Simple roofs use less material</span>
        </div>

        <div className={styles.inputGroup}>
          <label htmlFor="wallHeight">Wall Height (feet)</label>
          <select
            id="wallHeight"
            value={inputs.wallHeight}
            onChange={(e) => handleInputChange('wallHeight', Number(e.target.value))}
          >
            <option value={8}>8 feet (Standard)</option>
            <option value={9}>9 feet</option>
            <option value={10}>10 feet</option>
          </select>
        </div>

        <div className={styles.inputGroup}>
          <label htmlFor="finishLevel">Finish Level</label>
          <select
            id="finishLevel"
            value={inputs.finishLevel}
            onChange={(e) => handleInputChange('finishLevel', e.target.value)}
          >
            <option value="basic">Basic</option>
            <option value="standard">Standard</option>
            <option value="premium">Premium</option>
          </select>
          <span className={styles.hint}>Affects material quality and cost</span>
        </div>

        <button onClick={calculate} className={styles.calculateButton}>
          Estimate Materials
        </button>
      </div>

      {results && (
        <div className={styles.results}>
          <h3 className={styles.sectionTitle}>Material Estimates</h3>

          <div className={styles.resultCard + ' ' + styles.highlight}>
            <div className={styles.resultLabel}>Total Material Cost</div>
            <div className={styles.resultValue}>{formatCurrency(results.totalCost)}</div>
            <div className={styles.resultDetail}>
              Estimated cost for major materials
            </div>
          </div>

          <div className={styles.resultCard}>
            <div className={styles.resultLabel}>Concrete</div>
            <div className={styles.resultValue}>{formatNumber(results.concrete.cubicYards)} yd³</div>
            <div className={styles.resultDetail}>
              {formatCurrency(results.concrete.cost)} (Foundation & footings)
            </div>
          </div>

          <div className={styles.resultCard}>
            <div className={styles.resultLabel}>Framing Lumber</div>
            <div className={styles.resultValue}>{formatNumber(results.lumber.boardFeet)} bf</div>
            <div className={styles.resultDetail}>
              {formatCurrency(results.lumber.cost)} (Studs, joists, rafters)
            </div>
          </div>

          <div className={styles.resultCard}>
            <div className={styles.resultLabel}>Drywall</div>
            <div className={styles.resultValue}>{results.drywall.sheets} sheets</div>
            <div className={styles.resultDetail}>
              {formatCurrency(results.drywall.cost)} (4x8 sheets)
            </div>
          </div>

          <div className={styles.resultCard}>
            <div className={styles.resultLabel}>Roofing</div>
            <div className={styles.resultValue}>{formatNumber(results.roofing.squares)} sq</div>
            <div className={styles.resultDetail}>
              {formatCurrency(results.roofing.cost)} (Shingles & underlayment)
            </div>
          </div>

          <div className={styles.resultCard}>
            <div className={styles.resultLabel}>Flooring</div>
            <div className={styles.resultValue}>{formatNumber(results.flooring.squareFeet)} ft²</div>
            <div className={styles.resultDetail}>
              {formatCurrency(results.flooring.cost)} (Based on finish level)
            </div>
          </div>

          <div className={styles.resultCard}>
            <div className={styles.resultLabel}>Insulation</div>
            <div className={styles.resultValue}>{formatNumber(results.insulation.squareFeet)} ft²</div>
            <div className={styles.resultDetail}>
              {formatCurrency(results.insulation.cost)} (Walls & ceiling)
            </div>
          </div>

          <div className={styles.breakdown}>
            <h4>Important Notes</h4>
            <ul>
              <li>
                <strong>Waste Factor:</strong> These estimates include typical waste factors (10-15% for most materials).
                Always order 5-10% extra for critical items.
              </li>
              <li>
                <strong>What's NOT Included:</strong> Windows, doors, cabinets, appliances, HVAC equipment,
                electrical fixtures, plumbing fixtures, and many finish items.
              </li>
              <li>
                <strong>Regional Pricing:</strong> Material costs vary significantly by region.
                Use these estimates as a baseline and get local quotes.
              </li>
              <li>
                <strong>Bulk Discounts:</strong> You may receive 10-20% contractor discounts when ordering
                in bulk from lumber yards and suppliers.
              </li>
            </ul>
          </div>

          <div className={styles.cta}>
            <p>Ready to start planning your material orders?</p>
            <a href="/build-phases/framing" className={styles.ctaButton}>
              Learn About Build Phases
            </a>
          </div>
        </div>
      )}
      </div>
    </CalculatorCard>
  );
}
