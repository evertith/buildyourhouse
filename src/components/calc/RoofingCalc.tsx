'use client';

import { useMemo, useState } from 'react';
import CalcSheet, { BarRow } from './CalcSheet';
import { DimPair, Seg, SelectField } from './fields';
import { calculateRoofing, RoofingInputs } from '@/lib/calc/roofing';

const DEFAULTS: RoofingInputs = {
  lengthFt: 40,
  widthFt: 30,
  pitch: 6,
  overhangFt: 1,
  complexity: 'gable',
};

const SHAPE_LABEL: Record<RoofingInputs['complexity'], string> = {
  gable: 'Gable',
  hips: 'Hips',
  complex: 'Cut-up',
};

export default function RoofingCalc() {
  const [inputs, setInputs] = useState<RoofingInputs>(DEFAULTS);
  const set = <K extends keyof RoofingInputs>(key: K, value: RoofingInputs[K]) =>
    setInputs((prev) => ({ ...prev, [key]: value }));

  const result = useMemo(() => calculateRoofing(inputs), [inputs]);

  // Cost-share breakdown — comparable across lines measured in different
  // units (bundles vs. rolls vs. sticks), using range midpoints.
  const bars: BarRow[] = result.lines.map((l) => ({
    key: l.id,
    label: l.label.replace('Architectural shingles', 'Shingles').replace('Synthetic underlayment', 'Underlay').replace('Starter strip', 'Starter').replace('Ridge & hip cap', 'Ridge cap').replace('Roofing nails', 'Nails'),
    qty: ((l.costLow ?? 0) + (l.costHigh ?? 0)) / 2,
    valueLabel: `${l.qty} ${l.unit}`,
  }));

  return (
    <CalcSheet
      slug="roofing"
      sheetNo="TO-04"
      sheetTitle="Roofing takeoff"
      calculatorName="Roofing Calculator"
      result={result}
      bars={bars}
      barsLabel="Where the cost goes"
      finePrintBasis="a rectangular footprint, the pitch multiplier shown below, and complexity-based waste of 10–20%"
      inputsSummary={[
        { label: 'Footprint', value: `${inputs.lengthFt} × ${inputs.widthFt} ft` },
        { label: 'Pitch', value: `${inputs.pitch}/12` },
        { label: 'Overhang', value: `${inputs.overhangFt} ft` },
        { label: 'Roof shape', value: SHAPE_LABEL[inputs.complexity] },
      ]}
    >
      <DimPair
        label="Footprint"
        lengthValue={inputs.lengthFt}
        widthValue={inputs.widthFt}
        onLength={(v) => set('lengthFt', v)}
        onWidth={(v) => set('widthFt', v)}
        hint="House footprint at the walls — not the roof"
      />
      <SelectField
        label="Roof pitch"
        options={[
          { value: '4', label: '4/12' },
          { value: '5', label: '5/12' },
          { value: '6', label: '6/12' },
          { value: '7', label: '7/12' },
          { value: '8', label: '8/12' },
          { value: '9', label: '9/12' },
          { value: '10', label: '10/12' },
          { value: '12', label: '12/12' },
        ]}
        value={String(inputs.pitch)}
        onChange={(v) => set('pitch', Number(v) as RoofingInputs['pitch'])}
        hint="Rise per 12 inches of run — 6/12 is the suburban default"
      />
      <Seg
        label="Overhang"
        options={[{ value: 0, label: '0' }, { value: 1, label: '1 ft' }, { value: 2, label: '2 ft' }]}
        value={inputs.overhangFt}
        onChange={(v) => set('overhangFt', v as RoofingInputs['overhangFt'])}
      />
      <Seg
        label="Roof shape"
        options={[
          { value: 'gable', label: 'Gable' },
          { value: 'hips', label: 'Hips' },
          { value: 'complex', label: 'Cut-up' },
        ]}
        value={inputs.complexity}
        onChange={(v) => set('complexity', v as RoofingInputs['complexity'])}
        hint="Sets waste: gable 10%, hips 15%, cut-up 20%"
      />
    </CalcSheet>
  );
}
