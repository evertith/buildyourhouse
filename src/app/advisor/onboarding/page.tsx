'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { useAdvisor } from '@/lib/advisor-context';
import * as api from '@/lib/advisor-api';
import styles from '@/styles/AdvisorOnboarding.module.css';

const TOTAL_STEPS = 5;

const STATES = [
  { value: 'alabama', label: 'Alabama' }, { value: 'alaska', label: 'Alaska' },
  { value: 'arizona', label: 'Arizona' }, { value: 'arkansas', label: 'Arkansas' },
  { value: 'california', label: 'California' }, { value: 'colorado', label: 'Colorado' },
  { value: 'connecticut', label: 'Connecticut' }, { value: 'delaware', label: 'Delaware' },
  { value: 'florida', label: 'Florida' }, { value: 'georgia', label: 'Georgia' },
  { value: 'hawaii', label: 'Hawaii' }, { value: 'idaho', label: 'Idaho' },
  { value: 'illinois', label: 'Illinois' }, { value: 'indiana', label: 'Indiana' },
  { value: 'iowa', label: 'Iowa' }, { value: 'kansas', label: 'Kansas' },
  { value: 'kentucky', label: 'Kentucky' }, { value: 'louisiana', label: 'Louisiana' },
  { value: 'maine', label: 'Maine' }, { value: 'maryland', label: 'Maryland' },
  { value: 'massachusetts', label: 'Massachusetts' }, { value: 'michigan', label: 'Michigan' },
  { value: 'minnesota', label: 'Minnesota' }, { value: 'mississippi', label: 'Mississippi' },
  { value: 'missouri', label: 'Missouri' }, { value: 'montana', label: 'Montana' },
  { value: 'nebraska', label: 'Nebraska' }, { value: 'nevada', label: 'Nevada' },
  { value: 'new-hampshire', label: 'New Hampshire' }, { value: 'new-jersey', label: 'New Jersey' },
  { value: 'new-mexico', label: 'New Mexico' }, { value: 'new-york', label: 'New York' },
  { value: 'north-carolina', label: 'North Carolina' }, { value: 'north-dakota', label: 'North Dakota' },
  { value: 'ohio', label: 'Ohio' }, { value: 'oklahoma', label: 'Oklahoma' },
  { value: 'oregon', label: 'Oregon' }, { value: 'pennsylvania', label: 'Pennsylvania' },
  { value: 'rhode-island', label: 'Rhode Island' }, { value: 'south-carolina', label: 'South Carolina' },
  { value: 'south-dakota', label: 'South Dakota' }, { value: 'tennessee', label: 'Tennessee' },
  { value: 'texas', label: 'Texas' }, { value: 'utah', label: 'Utah' },
  { value: 'vermont', label: 'Vermont' }, { value: 'virginia', label: 'Virginia' },
  { value: 'washington', label: 'Washington' }, { value: 'west-virginia', label: 'West Virginia' },
  { value: 'wisconsin', label: 'Wisconsin' }, { value: 'wyoming', label: 'Wyoming' },
];

const PHASES = [
  { value: 'researching', label: 'Researching', desc: 'Still learning about owner-building' },
  { value: 'planning', label: 'Planning', desc: 'Securing land, plans, or financing' },
  { value: 'permitting', label: 'Permitting', desc: 'Working on permits and approvals' },
  { value: 'site-preparation', label: 'Under Construction', desc: 'Build is actively underway' },
];

const APPROACHES = [
  { value: 'diy', label: 'Mostly DIY', desc: 'I\'ll do most of the work myself' },
  { value: 'subs', label: 'Hiring Subs', desc: 'I\'ll manage subcontractors' },
  { value: 'mix', label: 'Mix of Both', desc: 'DIY some phases, hire for others' },
];

export default function OnboardingPage() {
  const router = useRouter();
  const { user, loading: authLoading } = useAdvisor();
  const [step, setStep] = useState(1);
  const [error, setError] = useState('');
  const [submitting, setSubmitting] = useState(false);

  // Form state
  const [state, setState] = useState('');
  const [county, setCounty] = useState('');
  const [phase, setPhase] = useState('');
  const [squareFootage, setSquareFootage] = useState('');
  const [stories, setStories] = useState('1');
  const [foundationType, setFoundationType] = useState('');
  const [buildApproach, setBuildApproach] = useState('mix');
  const [hasLand, setHasLand] = useState(false);
  const [hasPlans, setHasPlans] = useState(false);
  const [hasPermit, setHasPermit] = useState(false);
  const [hasLoan, setHasLoan] = useState(false);
  const [budgetRange, setBudgetRange] = useState('');
  const [timelineGoal, setTimelineGoal] = useState('');
  const [notes, setNotes] = useState('');

  useEffect(() => {
    if (!authLoading && !user) {
      router.push('/advisor/signup');
    }
  }, [authLoading, user, router]);

  const canAdvance = () => {
    switch (step) {
      case 1: return !!state;
      case 2: return !!phase;
      case 3: return true;
      case 4: return true;
      case 5: return true;
      default: return false;
    }
  };

  const handleSubmit = async () => {
    setError('');
    setSubmitting(true);

    try {
      const build = await api.createBuild({
        state,
        county: county || undefined,
        phase,
        square_footage: squareFootage ? parseInt(squareFootage) : undefined,
        stories: parseInt(stories),
        foundation_type: foundationType || undefined,
        build_approach: buildApproach,
        budget_range: budgetRange || undefined,
        timeline_goal: timelineGoal || undefined,
        has_land: hasLand ? 1 : 0,
        has_plans: hasPlans ? 1 : 0,
        has_permit: hasPermit ? 1 : 0,
        has_loan: hasLoan ? 1 : 0,
        notes: notes || undefined,
      } as Partial<api.Build>);

      // Store the active build ID
      localStorage.setItem('advisor_active_build', build.id);
      router.push('/advisor/chat');
    } catch (err) {
      if (err instanceof api.AdvisorApiError) {
        setError(err.message);
      } else {
        setError('Something went wrong. Please try again.');
      }
    } finally {
      setSubmitting(false);
    }
  };

  if (authLoading) return null;

  return (
    <div className={styles.container}>
      <div className={styles.card}>
        {/* Progress dots */}
        <div className={styles.progress}>
          {Array.from({ length: TOTAL_STEPS }, (_, i) => (
            <div
              key={i}
              className={`${styles.progressDot} ${i < step ? styles.progressDotActive : ''}`}
            />
          ))}
        </div>

        {error && <div className={styles.error}>{error}</div>}

        {/* Step 1: Location */}
        {step === 1 && (
          <>
            <h2 className={styles.title}>Where are you building?</h2>
            <p className={styles.description}>
              This helps us give you state-specific advice on permits, codes, and regulations.
            </p>

            <div className={styles.fieldGroup}>
              <label className={styles.fieldLabel} htmlFor="state">State *</label>
              <select
                id="state"
                className={styles.select}
                value={state}
                onChange={(e) => setState(e.target.value)}
              >
                <option value="">Select your state</option>
                {STATES.map(s => (
                  <option key={s.value} value={s.value}>{s.label}</option>
                ))}
              </select>
            </div>

            <div className={styles.fieldGroup}>
              <label className={styles.fieldLabel} htmlFor="county">County (optional)</label>
              <input
                id="county"
                type="text"
                className={styles.input}
                value={county}
                onChange={(e) => setCounty(e.target.value)}
                placeholder="e.g., Wake County"
              />
            </div>
          </>
        )}

        {/* Step 2: Phase */}
        {step === 2 && (
          <>
            <h2 className={styles.title}>Where are you in the process?</h2>
            <p className={styles.description}>
              We&apos;ll tailor our advice to your current stage.
            </p>

            <div className={styles.optionGrid}>
              {PHASES.map(p => (
                <div
                  key={p.value}
                  className={`${styles.optionCard} ${phase === p.value ? styles.optionCardSelected : ''}`}
                  onClick={() => setPhase(p.value)}
                >
                  <div className={styles.optionCardLabel}>{p.label}</div>
                  <div className={styles.optionCardDesc}>{p.desc}</div>
                </div>
              ))}
            </div>
          </>
        )}

        {/* Step 3: Build Details */}
        {step === 3 && (
          <>
            <h2 className={styles.title}>Tell us about your build</h2>
            <p className={styles.description}>
              All optional — fill in what you know. You can update this later.
            </p>

            <div className={styles.fieldGroup}>
              <label className={styles.fieldLabel} htmlFor="sqft">Approximate Square Footage</label>
              <input
                id="sqft"
                type="number"
                className={styles.input}
                value={squareFootage}
                onChange={(e) => setSquareFootage(e.target.value)}
                placeholder="e.g., 2000"
              />
            </div>

            <div className={styles.fieldGroup}>
              <label className={styles.fieldLabel} htmlFor="stories">Stories</label>
              <select
                id="stories"
                className={styles.select}
                value={stories}
                onChange={(e) => setStories(e.target.value)}
              >
                <option value="1">1 Story</option>
                <option value="2">2 Stories</option>
                <option value="3">3 Stories</option>
              </select>
            </div>

            <div className={styles.fieldGroup}>
              <label className={styles.fieldLabel} htmlFor="foundation">Foundation Type</label>
              <select
                id="foundation"
                className={styles.select}
                value={foundationType}
                onChange={(e) => setFoundationType(e.target.value)}
              >
                <option value="">Not sure yet</option>
                <option value="slab">Slab</option>
                <option value="crawl-space">Crawl Space</option>
                <option value="basement">Basement</option>
              </select>
            </div>

            <div className={styles.fieldGroup}>
              <label className={styles.fieldLabel}>Build Approach</label>
              <div className={styles.optionGrid}>
                {APPROACHES.map(a => (
                  <div
                    key={a.value}
                    className={`${styles.optionCard} ${buildApproach === a.value ? styles.optionCardSelected : ''}`}
                    onClick={() => setBuildApproach(a.value)}
                  >
                    <div className={styles.optionCardLabel}>{a.label}</div>
                    <div className={styles.optionCardDesc}>{a.desc}</div>
                  </div>
                ))}
              </div>
            </div>
          </>
        )}

        {/* Step 4: What You Have */}
        {step === 4 && (
          <>
            <h2 className={styles.title}>What do you have so far?</h2>
            <p className={styles.description}>
              Check everything that applies. This helps us understand where you need the most help.
            </p>

            <div className={styles.checkboxGroup}>
              <label className={styles.checkbox}>
                <input type="checkbox" checked={hasLand} onChange={(e) => setHasLand(e.target.checked)} />
                <span>I have land (or a lot under contract)</span>
              </label>
              <label className={styles.checkbox}>
                <input type="checkbox" checked={hasPlans} onChange={(e) => setHasPlans(e.target.checked)} />
                <span>I have house plans (or working with a designer)</span>
              </label>
              <label className={styles.checkbox}>
                <input type="checkbox" checked={hasPermit} onChange={(e) => setHasPermit(e.target.checked)} />
                <span>I have a building permit (or in review)</span>
              </label>
              <label className={styles.checkbox}>
                <input type="checkbox" checked={hasLoan} onChange={(e) => setHasLoan(e.target.checked)} />
                <span>I have financing (construction loan or cash)</span>
              </label>
            </div>
          </>
        )}

        {/* Step 5: Budget & Timeline */}
        {step === 5 && (
          <>
            <h2 className={styles.title}>Budget and timeline</h2>
            <p className={styles.description}>
              Optional — helps us give more realistic cost and time estimates.
            </p>

            <div className={styles.fieldGroup}>
              <label className={styles.fieldLabel} htmlFor="budget">Budget Range</label>
              <select
                id="budget"
                className={styles.select}
                value={budgetRange}
                onChange={(e) => setBudgetRange(e.target.value)}
              >
                <option value="">Prefer not to say</option>
                <option value="under-100k">Under $100,000</option>
                <option value="100k-200k">$100,000 - $200,000</option>
                <option value="200k-350k">$200,000 - $350,000</option>
                <option value="350k-500k">$350,000 - $500,000</option>
                <option value="over-500k">Over $500,000</option>
              </select>
            </div>

            <div className={styles.fieldGroup}>
              <label className={styles.fieldLabel} htmlFor="timeline">Timeline Goal</label>
              <select
                id="timeline"
                className={styles.select}
                value={timelineGoal}
                onChange={(e) => setTimelineGoal(e.target.value)}
              >
                <option value="">No specific goal</option>
                <option value="6-months">6 months</option>
                <option value="12-months">12 months</option>
                <option value="18-months">18 months</option>
                <option value="24-months">24 months</option>
                <option value="flexible">Flexible / no rush</option>
              </select>
            </div>

            <div className={styles.fieldGroup}>
              <label className={styles.fieldLabel} htmlFor="notes">Anything else we should know?</label>
              <textarea
                id="notes"
                className={styles.input}
                value={notes}
                onChange={(e) => setNotes(e.target.value)}
                placeholder="e.g., building on a slope, need wheelchair accessible, first-time builder..."
                rows={3}
                style={{ resize: 'vertical' }}
              />
            </div>
          </>
        )}

        {/* Navigation buttons */}
        <div className={styles.buttons}>
          {step > 1 && (
            <button className={styles.backButton} onClick={() => setStep(s => s - 1)}>
              Back
            </button>
          )}

          {step < TOTAL_STEPS ? (
            <button
              className={styles.nextButton}
              onClick={() => setStep(s => s + 1)}
              disabled={!canAdvance()}
            >
              Continue
            </button>
          ) : (
            <button
              className={styles.nextButton}
              onClick={handleSubmit}
              disabled={submitting}
            >
              {submitting ? 'Setting up...' : 'Start Chatting'}
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
