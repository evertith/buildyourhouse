'use client';

import { useMemo, useState } from 'react';
import s from '@/styles/CalcSheet.module.css';
import CalcSheet, { BarRow } from './CalcSheet';
import { NumberField, Seg } from './fields';
import { calculateTimeline, TimelineInputs } from '@/lib/calc/timeline';

const DEFAULTS: TimelineInputs = {
  homeSizeSqFt: 2000,
  hoursPerWeek: 20,
  diyPercentage: 50,
  experienceLevel: 'intermediate',
  helpers: 0,
};

const EXPERIENCE_LABEL: Record<TimelineInputs['experienceLevel'], string> = {
  beginner: 'Beginner — first build',
  intermediate: 'Intermediate — some experience',
  experienced: 'Experienced — multiple projects',
};

export default function TimelineCalc() {
  const [inputs, setInputs] = useState<TimelineInputs>(DEFAULTS);
  const set = <K extends keyof TimelineInputs>(key: K, value: TimelineInputs[K]) =>
    setInputs((prev) => ({ ...prev, [key]: value }));

  const result = useMemo(() => calculateTimeline(inputs), [inputs]);

  const bars: BarRow[] = result.phases.map((p) => ({
    key: p.id,
    label: p.name.replace('Planning & Permitting', 'Planning').replace('Insulation & Drywall', 'Insul./drywall').replace('Interior Finishes', 'Interior').replace('Final & Exterior', 'Final'),
    qty: p.weeks,
    valueLabel: `${p.weeks} ${p.weeks === 1 ? 'week' : 'weeks'}`,
  }));

  return (
    <CalcSheet
      slug="timeline-estimator"
      sheetNo="W-03"
      sheetTitle="Schedule worksheet"
      calculatorName="Timeline Estimator"
      inputsLabel="Build profile"
      result={result}
      bars={bars}
      barsLabel="Where the weeks go"
      finePrintBasis="1.75 personal hours per square foot before your experience, helpers, and DIY share adjust it, and an uninterrupted run at your stated hours"
      inputsSummary={[
        { label: 'Home size', value: `${inputs.homeSizeSqFt.toLocaleString('en-US')} sq ft` },
        { label: 'Hours per week', value: `${inputs.hoursPerWeek} hrs` },
        { label: 'DIY share', value: `${inputs.diyPercentage}%` },
        { label: 'Experience', value: EXPERIENCE_LABEL[inputs.experienceLevel] },
        { label: 'Regular helpers', value: String(inputs.helpers) },
      ]}
    >
      <NumberField
        label="Home size"
        unit="sq ft"
        value={inputs.homeSizeSqFt}
        onChange={(v) => set('homeSizeSqFt', v)}
        step={100}
        hint="Finished, conditioned square footage"
      />
      <NumberField
        label="Hours per week"
        unit="hrs"
        value={inputs.hoursPerWeek}
        onChange={(v) => set('hoursPerWeek', v)}
        step={5}
        hint="Evenings, weekends, and vacation time — what you can actually hold week after week"
      />
      <NumberField
        label="DIY share"
        unit="%"
        value={inputs.diyPercentage}
        onChange={(v) => set('diyPercentage', v)}
        step={10}
        hint="How much of the work you keep instead of subbing it out"
      />
      <Seg
        label="Experience"
        options={[
          { value: 'beginner', label: 'First build' },
          { value: 'intermediate', label: 'Some' },
          { value: 'experienced', label: 'Seasoned' },
        ]}
        value={inputs.experienceLevel}
        onChange={(v) => set('experienceLevel', v as TimelineInputs['experienceLevel'])}
        hint="A first build runs 1.4× the hours; multiple projects behind you, 0.8×"
      />
      <Seg
        label="Regular helpers"
        options={[0, 1, 2, 3, 4, 5].map((n) => ({ value: n, label: String(n) }))}
        value={inputs.helpers}
        onChange={(v) => set('helpers', v as number)}
        hint="Friends and family who consistently show up — each one adds 60% more output, not 100%"
      />

      {result.warnings.length > 0 && (
        <div className={s.field}>
          <span className={s.fieldLabel}>Reality check</span>
          {result.warnings.map((w) => (
            <span key={w} className={s.fieldHint}>
              {w}
            </span>
          ))}
        </div>
      )}
    </CalcSheet>
  );
}
