'use client';

import { useMemo, useState } from 'react';
import CalcSheet, { BarRow } from './CalcSheet';
import { DimPair, Seg } from './fields';
import { calculateFraming, FramingInputs } from '@/lib/calc/framing';

const DEFAULTS: FramingInputs = {
  lengthFt: 40,
  widthFt: 30,
  stories: 1,
  wallHeightFt: 8,
  studSpacing: 16,
  studSize: '2x4',
  includeInterior: true,
};

export default function FramingCalc() {
  const [inputs, setInputs] = useState<FramingInputs>(DEFAULTS);
  const set = <K extends keyof FramingInputs>(key: K, value: FramingInputs[K]) =>
    setInputs((prev) => ({ ...prev, [key]: value }));

  const result = useMemo(() => calculateFraming(inputs), [inputs]);

  // Cost-share breakdown — comparable across lines measured in different
  // units (studs vs. sheets vs. boards), using range midpoints.
  const bars: BarRow[] = result.lines.map((l) => ({
    key: l.id,
    label: l.label.replace('Exterior wall studs', 'Ext. studs').replace('Interior partition studs', 'Int. studs').replace('Wall sheathing', 'Sheathing').replace(' stock', 's'),
    qty: ((l.costLow ?? 0) + (l.costHigh ?? 0)) / 2,
    valueLabel: `${l.qty} ${l.unit}`,
  }));

  return (
    <CalcSheet
      slug="framing-lumber"
      sheetNo="TO-01"
      sheetTitle="Framing takeoff"
      calculatorName="Framing Lumber Calculator"
      result={result}
      bars={bars}
      barsLabel="Where the cost goes"
      finePrintBasis={`${inputs.studSpacing}" o.c. stud walls with doubled top plates, one opening per ~120 sq ft, and 4×8 OSB sheathing with 10% waste`}
      inputsSummary={[
        { label: 'Footprint', value: `${inputs.lengthFt} × ${inputs.widthFt} ft` },
        { label: 'Stories', value: String(inputs.stories) },
        { label: 'Wall height', value: `${inputs.wallHeightFt} ft` },
        { label: 'Stud spacing', value: `${inputs.studSpacing}" on-center` },
        { label: 'Exterior studs', value: inputs.studSize === '2x4' ? '2×4' : '2×6' },
        { label: 'Interior walls', value: inputs.includeInterior ? 'Included' : 'Exterior only' },
      ]}
    >
      <DimPair
        label="Footprint"
        lengthValue={inputs.lengthFt}
        widthValue={inputs.widthFt}
        onLength={(v) => set('lengthFt', v)}
        onWidth={(v) => set('widthFt', v)}
        hint="Outside wall to outside wall, per floor"
      />
      <Seg
        label="Stories"
        options={[{ value: 1, label: '1' }, { value: 2, label: '2' }, { value: 3, label: '3' }]}
        value={inputs.stories}
        onChange={(v) => set('stories', v as FramingInputs['stories'])}
      />
      <Seg
        label="Wall height"
        options={[{ value: 8, label: '8 ft' }, { value: 9, label: '9 ft' }, { value: 10, label: '10 ft' }]}
        value={inputs.wallHeightFt}
        onChange={(v) => set('wallHeightFt', v as FramingInputs['wallHeightFt'])}
      />
      <Seg
        label="Stud spacing"
        options={[{ value: 16, label: '16" OC' }, { value: 24, label: '24" OC' }]}
        value={inputs.studSpacing}
        onChange={(v) => set('studSpacing', v as FramingInputs['studSpacing'])}
        hint='16" is standard; 24" needs 2×6 walls in most codes'
      />
      <Seg
        label="Exterior stud size"
        options={[{ value: '2x4', label: '2×4' }, { value: '2x6', label: '2×6' }]}
        value={inputs.studSize}
        onChange={(v) => set('studSize', v as FramingInputs['studSize'])}
        hint="2×6 fits R-19/R-21 insulation; many cold-climate codes require it"
      />
      <Seg
        label="Interior walls"
        options={[{ value: 'yes', label: 'Included' }, { value: 'no', label: 'Exterior only' }]}
        value={inputs.includeInterior ? 'yes' : 'no'}
        onChange={(v) => set('includeInterior', v === 'yes')}
        hint="Included = 1 lf of partition per 4 sq ft of floor"
      />
    </CalcSheet>
  );
}
