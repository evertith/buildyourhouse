'use client';

import { useState } from 'react';
import { calculateTimelineEstimate, TimelineEstimatorInputs, TimelineEstimatorResults } from '@/lib/calculators';
import CalculatorCard from '@/components/CalculatorCard';
import styles from '@/styles/Calculator.module.css';

export default function TimelineEstimatorCalculator() {
  const [inputs, setInputs] = useState<TimelineEstimatorInputs>({
    homeSize: 2000,
    hoursPerWeek: 20,
    diyPercentage: 50,
    experienceLevel: 'intermediate',
    helpers: 0
  });

  const [results, setResults] = useState<TimelineEstimatorResults | null>(null);

  const handleInputChange = (field: keyof TimelineEstimatorInputs, value: number | string) => {
    setInputs(prev => ({ ...prev, [field]: value }));
  };

  const calculate = () => {
    const calculatedResults = calculateTimelineEstimate(inputs);
    setResults(calculatedResults);
  };

  const formatNumber = (value: number) => {
    return new Intl.NumberFormat('en-US').format(value);
  };

  return (
    <CalculatorCard
      title="Timeline Estimator"
      description="Estimate how long your DIY home build will take based on your schedule and experience"
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
          <label htmlFor="hoursPerWeek">Hours Per Week You Can Work</label>
          <input
            id="hoursPerWeek"
            type="number"
            value={inputs.hoursPerWeek}
            onChange={(e) => handleInputChange('hoursPerWeek', Number(e.target.value))}
            min="5"
            max="60"
            step="5"
          />
          <span className={styles.hint}>Include evenings, weekends, and vacation time</span>
        </div>

        <div className={styles.inputGroup}>
          <label htmlFor="diyPercentage">DIY Percentage (%)</label>
          <input
            id="diyPercentage"
            type="number"
            value={inputs.diyPercentage}
            onChange={(e) => handleInputChange('diyPercentage', Number(e.target.value))}
            min="0"
            max="100"
            step="10"
          />
          <span className={styles.hint}>How much will you do yourself vs. hiring out?</span>
        </div>

        <div className={styles.inputGroup}>
          <label htmlFor="experienceLevel">Your Experience Level</label>
          <select
            id="experienceLevel"
            value={inputs.experienceLevel}
            onChange={(e) => handleInputChange('experienceLevel', e.target.value)}
          >
            <option value="beginner">Beginner (First Build)</option>
            <option value="intermediate">Intermediate (Some Experience)</option>
            <option value="experienced">Experienced (Multiple Projects)</option>
          </select>
        </div>

        <div className={styles.inputGroup}>
          <label htmlFor="helpers">Regular Helpers</label>
          <input
            id="helpers"
            type="number"
            value={inputs.helpers}
            onChange={(e) => handleInputChange('helpers', Number(e.target.value))}
            min="0"
            max="5"
            step="1"
          />
          <span className={styles.hint}>Friends/family who will consistently help</span>
        </div>

        <button onClick={calculate} className={styles.calculateButton}>
          Estimate Timeline
        </button>
      </div>

      {results && (
        <div className={styles.results}>
          <h3 className={styles.sectionTitle}>Your Estimated Timeline</h3>

          <div className={styles.resultCard + ' ' + styles.highlight}>
            <div className={styles.resultLabel}>Total Build Time</div>
            <div className={styles.resultValue}>{results.totalMonths} months</div>
            <div className={styles.resultDetail}>
              Approximately {results.totalWeeks} weeks
            </div>
          </div>

          <div className={styles.resultCard}>
            <div className={styles.resultLabel}>Total Hours</div>
            <div className={styles.resultValue}>{formatNumber(results.totalHours)}</div>
            <div className={styles.resultDetail}>
              Your personal time investment
            </div>
          </div>

          <div className={styles.resultCard}>
            <div className={styles.resultLabel}>Weekly Commitment</div>
            <div className={styles.resultValue}>{inputs.hoursPerWeek} hrs</div>
            <div className={styles.resultDetail}>
              {(inputs.hoursPerWeek / 40 * 100).toFixed(0)}% of a full-time job
            </div>
          </div>

          <div className={styles.disclaimer}>
            Estimate only — not financial or scheduling advice. Actual build times vary
            widely with weather, permits, inspections, material delays, and life events.
          </div>

          <div className={styles.breakdown}>
            <h4>Phase-by-Phase Timeline</h4>
            <ul style={{ listStyle: 'none', padding: 0 }}>
              {results.phases.map((phase, index) => (
                <li key={index} style={{ marginBottom: '1rem', paddingLeft: '1.8rem', position: 'relative' }}>
                  <span style={{ position: 'absolute', left: 0, top: '0.1rem', fontSize: '1.1rem' }}>✓</span>
                  <strong style={{ color: 'var(--color-primary)', display: 'inline' }}>{phase.name}:</strong> {phase.weeks} weeks
                  <br />
                  <span style={{ fontSize: '0.9rem', color: 'var(--color-text-light)' }}>
                    {phase.description}
                  </span>
                </li>
              ))}
            </ul>
          </div>

          {results.warningFactors.length > 0 && (
            <div className={styles.breakdown} style={{ backgroundColor: '#fff3cd', marginTop: '1.5rem' }}>
              <h4 style={{ color: '#856404' }}>Reality Check</h4>
              <ul style={{ listStyle: 'none', padding: 0 }}>
                {results.warningFactors.map((warning, index) => (
                  <li key={index} style={{ marginBottom: '0.5rem', paddingLeft: '1.5rem', position: 'relative' }}>
                    <span style={{ position: 'absolute', left: 0, color: '#856404' }}>⚠</span>
                    {warning}
                  </li>
                ))}
              </ul>
            </div>
          )}

          <div className={styles.breakdown}>
            <h4>Timeline Tips</h4>
            <ul>
              <li>
                <strong>Weather Delays:</strong> Add 2-4 weeks for weather-related delays,
                especially if building through winter.
              </li>
              <li>
                <strong>Permit Wait Times:</strong> Some jurisdictions take 4-8 weeks for permit approval.
                Start this process early!
              </li>
              <li>
                <strong>Learning Curve:</strong> First-time builders should add 20-30% to estimated times
                for learning new skills.
              </li>
              <li>
                <strong>Inspection Delays:</strong> Failed inspections or scheduling delays can add
                1-2 weeks per phase.
              </li>
              <li>
                <strong>Life Happens:</strong> Plan for vacations, illness, work conflicts, and
                burnout. Few builds go exactly as planned.
              </li>
            </ul>
          </div>

          <div className={styles.cta}>
            <p>Want to optimize your build schedule?</p>
            <a href="/timing-and-scheduling" className={styles.ctaButton}>
              Learn About Scheduling
            </a>
          </div>
        </div>
      )}
      </div>
    </CalculatorCard>
  );
}
