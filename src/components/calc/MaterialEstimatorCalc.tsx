'use client';

import { useMemo, useState } from 'react';
import CalcSheet, { BarRow } from './CalcSheet';
import { NumberField, Seg } from './fields';
import { formatCurrency } from '@/lib/calc/format';
import { calculateMaterialEstimator, MaterialEstimatorInputs } from '@/lib/calc/materialEstimator';

const DEFAULTS: MaterialEstimatorInputs = {
  homeSizeSqFt: 2000,
  stories: 1,
  roofComplexity: 'moderate',
  wallHeightFt: 8,
  finishLevel: 'standard',
};

const BAR_LABEL: Record<string, string> = {
  concrete: 'Concrete',
  lumber: 'Lumber',
  drywall: 'Drywall',
  roofing: 'Roofing',
  flooring: 'Flooring',
  insulation: 'Insulation',
};

const ROOF_SUMMARY: Record<MaterialEstimatorInputs['roofComplexity'], string> = {
  simple: 'Simple gable',
  moderate: 'Hip or mixed',
  complex: 'Cut-up, multiple valleys',
};

const FINISH_SUMMARY: Record<MaterialEstimatorInputs['finishLevel'], string> = {
  basic: 'Basic',
  standard: 'Standard',
  premium: 'Premium',
};

export default function MaterialEstimatorCalc() {
  const [inputs, setInputs] = useState<MaterialEstimatorInputs>(DEFAULTS);
  const set = <K extends keyof MaterialEstimatorInputs>(key: K, value: MaterialEstimatorInputs[K]) =>
    setInputs((prev) => ({ ...prev, [key]: value }));

  const result = useMemo(() => calculateMaterialEstimator(inputs), [inputs]);

  // Systems priced in different units (yd³, bf, sheets, squares, ft²) only
  // compare on dollars — bars carry the cost share, the schedule above
  // carries the quantities.
  const bars: BarRow[] = result.lines.map((l) => {
    const mid = ((l.costLow ?? 0) + (l.costHigh ?? 0)) / 2;
    return {
      key: l.id,
      label: BAR_LABEL[l.id] ?? l.label,
      qty: mid,
      valueLabel: formatCurrency(mid),
    };
  });

  return (
    <CalcSheet
      slug="material-estimator"
      sheetNo="W-02"
      sheetTitle="Whole-house takeoff"
      calculatorName="Whole-House Material Estimator"
      inputsLabel="Project profile"
      result={result}
      bars={bars}
      barsLabel="Where the cost goes"
      finePrintBasis={`a rectangular 1.5:1 footprint, ${inputs.wallHeightFt}-ft walls, and 1 linear foot of interior partition per 4 sq ft of floor`}
      inputsSummary={[
        { label: 'Finished area', value: `${inputs.homeSizeSqFt.toLocaleString('en-US')} sq ft` },
        { label: 'Stories', value: String(inputs.stories) },
        { label: 'Wall height', value: `${inputs.wallHeightFt} ft` },
        { label: 'Roof', value: ROOF_SUMMARY[inputs.roofComplexity] },
        { label: 'Finish level', value: FINISH_SUMMARY[inputs.finishLevel] },
      ]}
    >
      <NumberField
        label="Finished square footage"
        unit="sq ft"
        value={inputs.homeSizeSqFt}
        onChange={(v) => set('homeSizeSqFt', v)}
        min={500}
        step={100}
        hint="Heated, finished area — all floors added together"
      />
      <Seg
        label="Stories"
        options={[
          { value: 1, label: '1' },
          { value: 2, label: '2' },
          { value: 3, label: '3' },
        ]}
        value={inputs.stories}
        onChange={(v) => set('stories', v as MaterialEstimatorInputs['stories'])}
        hint="Footprint = finished area ÷ stories, so a 2-story pours half the slab"
      />
      <Seg
        label="Wall height"
        options={[
          { value: 8, label: '8 ft' },
          { value: 9, label: '9 ft' },
          { value: 10, label: '10 ft' },
        ]}
        value={inputs.wallHeightFt}
        onChange={(v) => set('wallHeightFt', v as MaterialEstimatorInputs['wallHeightFt'])}
      />
      <Seg
        label="Roof complexity"
        options={[
          { value: 'simple', label: 'Gable' },
          { value: 'moderate', label: 'Hip · mixed' },
          { value: 'complex', label: 'Cut-up' },
        ]}
        value={inputs.roofComplexity}
        onChange={(v) => set('roofComplexity', v as MaterialEstimatorInputs['roofComplexity'])}
        hint="Roof area as a multiple of footprint: gable 1.1, hip or mixed 1.3, multiple valleys 1.5"
      />
      <Seg
        label="Finish level"
        options={[
          { value: 'basic', label: 'Basic' },
          { value: 'standard', label: 'Standard' },
          { value: 'premium', label: 'Premium' },
        ]}
        value={inputs.finishLevel}
        onChange={(v) => set('finishLevel', v as MaterialEstimatorInputs['finishLevel'])}
        hint="Sets material grade — board thickness, shingle line, flooring, and R-value"
      />
    </CalcSheet>
  );
}
