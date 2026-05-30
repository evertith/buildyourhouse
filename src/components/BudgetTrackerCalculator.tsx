'use client';

import { useState } from 'react';
import { calculateBudgetTracker, BudgetTrackerInputs, BudgetTrackerResults, BudgetPhase } from '@/lib/calculators';
import CalculatorCard from '@/components/CalculatorCard';
import styles from '@/styles/Calculator.module.css';

export default function BudgetTrackerCalculator() {
  const [contingency, setContingency] = useState(15);
  const [phases, setPhases] = useState<BudgetPhase[]>([
    { name: 'Site Prep & Foundation', budgeted: 45000, actual: 0 },
    { name: 'Framing & Exterior', budgeted: 65000, actual: 0 },
    { name: 'Rough-Ins (MEP)', budgeted: 40000, actual: 0 },
    { name: 'Insulation & Drywall', budgeted: 25000, actual: 0 },
    { name: 'Interior Finishes', budgeted: 50000, actual: 0 },
    { name: 'Final & Landscaping', budgeted: 25000, actual: 0 }
  ]);

  const [results, setResults] = useState<BudgetTrackerResults | null>(null);

  const handlePhaseChange = (index: number, field: 'budgeted' | 'actual', value: number) => {
    const newPhases = [...phases];
    newPhases[index][field] = value;
    setPhases(newPhases);
  };

  const handlePhaseNameChange = (index: number, value: string) => {
    const newPhases = [...phases];
    newPhases[index].name = value;
    setPhases(newPhases);
  };

  const addPhase = () => {
    setPhases([...phases, { name: 'New Phase', budgeted: 0, actual: 0 }]);
  };

  const removePhase = (index: number) => {
    if (phases.length > 1) {
      const newPhases = phases.filter((_, i) => i !== index);
      setPhases(newPhases);
    }
  };

  const calculate = () => {
    const inputs: BudgetTrackerInputs = {
      phases,
      contingency
    };
    const calculatedResults = calculateBudgetTracker(inputs);
    setResults(calculatedResults);
  };

  const formatCurrency = (value: number) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      maximumFractionDigits: 0
    }).format(value);
  };

  const getStatusColor = (status: 'under' | 'on-track' | 'over') => {
    if (status === 'under') return 'var(--color-success)';
    if (status === 'over') return '#dc3545';
    return 'var(--color-warning)';
  };

  const getStatusLabel = (status: 'under' | 'on-track' | 'over') => {
    if (status === 'under') return 'Under Budget';
    if (status === 'over') return 'Over Budget';
    return 'On Track';
  };

  return (
    <CalculatorCard
      title="Budget Tracker"
      description="Track your actual spending against budgeted amounts for each build phase"
    >
      <div className={styles.calculator}>
        <div className={styles.inputs}>
          <h3 className={styles.sectionTitle}>Budget Input</h3>

        <div className={styles.inputGroup}>
          <label htmlFor="contingency">Contingency Reserve (%)</label>
          <input
            id="contingency"
            type="number"
            value={contingency}
            onChange={(e) => setContingency(Number(e.target.value))}
            min="5"
            max="30"
            step="1"
          />
          <span className={styles.hint}>Typically 10-20% of total budget</span>
        </div>

        <div style={{ marginTop: '2rem' }}>
          <h4 style={{ fontSize: '1.1rem', marginBottom: '1rem' }}>Build Phases</h4>
          {phases.map((phase, index) => (
            <div key={index} style={{
              backgroundColor: 'var(--color-bg-light)',
              padding: '1rem',
              borderRadius: '8px',
              marginBottom: '1rem'
            }}>
              <div className={styles.inputGroup} style={{ marginBottom: '0.5rem' }}>
                <label htmlFor={`phase-name-${index}`}>Phase Name</label>
                <input
                  id={`phase-name-${index}`}
                  type="text"
                  value={phase.name}
                  onChange={(e) => handlePhaseNameChange(index, e.target.value)}
                />
              </div>
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '0.5rem' }}>
                <div className={styles.inputGroup} style={{ marginBottom: 0 }}>
                  <label htmlFor={`budgeted-${index}`}>Budgeted</label>
                  <input
                    id={`budgeted-${index}`}
                    type="number"
                    value={phase.budgeted}
                    onChange={(e) => handlePhaseChange(index, 'budgeted', Number(e.target.value))}
                    min="0"
                    step="1000"
                  />
                </div>
                <div className={styles.inputGroup} style={{ marginBottom: 0 }}>
                  <label htmlFor={`actual-${index}`}>Actual Spent</label>
                  <input
                    id={`actual-${index}`}
                    type="number"
                    value={phase.actual}
                    onChange={(e) => handlePhaseChange(index, 'actual', Number(e.target.value))}
                    min="0"
                    step="1000"
                  />
                </div>
              </div>
              {phases.length > 1 && (
                <button
                  onClick={() => removePhase(index)}
                  style={{
                    marginTop: '0.5rem',
                    padding: '0.5rem 1rem',
                    backgroundColor: '#dc3545',
                    color: 'white',
                    border: 'none',
                    borderRadius: '5px',
                    cursor: 'pointer',
                    fontSize: '0.9rem'
                  }}
                >
                  Remove Phase
                </button>
              )}
            </div>
          ))}
          <button
            onClick={addPhase}
            style={{
              width: '100%',
              padding: '0.75rem',
              backgroundColor: 'var(--color-secondary)',
              color: 'white',
              border: 'none',
              borderRadius: '8px',
              cursor: 'pointer',
              fontSize: '1rem',
              fontWeight: '600'
            }}
          >
            Add Phase
          </button>
        </div>

        <button onClick={calculate} className={styles.calculateButton} style={{ marginTop: '1.5rem' }}>
          Analyze Budget
        </button>
      </div>

      {results && (
        <div className={styles.results}>
          <h3 className={styles.sectionTitle}>Budget Analysis</h3>

          <div className={styles.resultCard + ' ' + styles.highlight}>
            <div className={styles.resultLabel}>Budget Status</div>
            <div className={styles.resultValue} style={{
              color: 'white',
              fontSize: results.totalVariance >= 0 ? '2.5rem' : '2rem'
            }}>
              {results.totalVariance >= 0 ? formatCurrency(results.totalVariance) : formatCurrency(Math.abs(results.totalVariance))}
            </div>
            <div className={styles.resultDetail}>
              {results.totalVariance >= 0 ? 'Under Budget' : 'Over Budget'}
              ({Math.abs(results.variancePercentage).toFixed(1)}%)
            </div>
          </div>

          <div className={styles.resultCard}>
            <div className={styles.resultLabel}>Total Budgeted</div>
            <div className={styles.resultValue}>{formatCurrency(results.totalBudgeted)}</div>
            <div className={styles.resultDetail}>
              Your planned total spend
            </div>
          </div>

          <div className={styles.resultCard}>
            <div className={styles.resultLabel}>Total Actual</div>
            <div className={styles.resultValue}>{formatCurrency(results.totalActual)}</div>
            <div className={styles.resultDetail}>
              What you've actually spent
            </div>
          </div>

          <div className={styles.resultCard}>
            <div className={styles.resultLabel}>Contingency Reserve</div>
            <div className={styles.resultValue}>{formatCurrency(results.contingencyAmount)}</div>
            <div className={styles.resultDetail}>
              {formatCurrency(results.contingencyRemaining)} remaining
            </div>
          </div>

          <div className={styles.disclaimer}>
            Estimate only — not financial advice. This tracker is a planning aid, not a
            substitute for a professional cost estimate, accounting, or your lender's
            requirements. Verify figures before making spending decisions.
          </div>

          <div className={styles.breakdown}>
            <h4>Phase-by-Phase Breakdown</h4>
            <div style={{ overflowX: 'auto' }}>
              <table style={{ width: '100%', borderCollapse: 'collapse' }}>
                <thead>
                  <tr style={{ borderBottom: '2px solid var(--color-border)' }}>
                    <th style={{ textAlign: 'left', padding: '0.5rem' }}>Phase</th>
                    <th style={{ textAlign: 'right', padding: '0.5rem' }}>Budgeted</th>
                    <th style={{ textAlign: 'right', padding: '0.5rem' }}>Actual</th>
                    <th style={{ textAlign: 'right', padding: '0.5rem' }}>Variance</th>
                    <th style={{ textAlign: 'center', padding: '0.5rem' }}>Status</th>
                  </tr>
                </thead>
                <tbody>
                  {results.phaseAnalysis.map((phase, index) => (
                    <tr key={index} style={{ borderBottom: '1px solid var(--color-border)' }}>
                      <td style={{ padding: '0.75rem 0.5rem' }}>{phase.name}</td>
                      <td style={{ textAlign: 'right', padding: '0.75rem 0.5rem' }}>
                        {formatCurrency(phase.budgeted)}
                      </td>
                      <td style={{ textAlign: 'right', padding: '0.75rem 0.5rem' }}>
                        {formatCurrency(phase.actual)}
                      </td>
                      <td style={{
                        textAlign: 'right',
                        padding: '0.75rem 0.5rem',
                        color: phase.variance >= 0 ? 'var(--color-success)' : '#dc3545',
                        fontWeight: '600'
                      }}>
                        {phase.variance >= 0 ? '+' : ''}{formatCurrency(phase.variance)}
                      </td>
                      <td style={{ textAlign: 'center', padding: '0.75rem 0.5rem' }}>
                        <span style={{
                          padding: '0.25rem 0.75rem',
                          borderRadius: '12px',
                          backgroundColor: getStatusColor(phase.status),
                          color: 'white',
                          fontSize: '0.85rem',
                          fontWeight: '600'
                        }}>
                          {getStatusLabel(phase.status)}
                        </span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

          {results.recommendations.length > 0 && (
            <div className={styles.breakdown} style={{
              backgroundColor: results.overallStatus === 'over' ? '#fff3cd' : 'var(--color-bg-light)'
            }}>
              <h4 style={{
                color: results.overallStatus === 'over' ? '#856404' : 'var(--color-text)'
              }}>
                Recommendations
              </h4>
              <ul style={{ listStyle: 'none', padding: 0 }}>
                {results.recommendations.map((rec, index) => (
                  <li key={index} style={{
                    marginBottom: '0.5rem',
                    paddingLeft: '1.5rem',
                    position: 'relative'
                  }}>
                    <span style={{
                      position: 'absolute',
                      left: 0,
                      color: rec.includes('ALERT') ? '#dc3545' : results.overallStatus === 'over' ? '#856404' : 'var(--color-primary)'
                    }}>
                      {rec.includes('ALERT') ? '⚠' : rec.includes('Under budget') ? '✓' : '→'}
                    </span>
                    {rec}
                  </li>
                ))}
              </ul>
            </div>
          )}

          <div className={styles.cta}>
            <p>Need help managing your budget?</p>
            <a href="/feasibility/cost-savings-calculator" className={styles.ctaButton}>
              Calculate Your Savings
            </a>
          </div>
        </div>
      )}
      </div>
    </CalculatorCard>
  );
}
