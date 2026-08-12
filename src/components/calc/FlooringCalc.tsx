'use client';

import { useMemo, useState } from 'react';
import CalcSheet from './CalcSheet';
import { NumberField, Seg, SelectField } from './fields';
import { calculateFlooring, FlooringInputs, FlooringMaterial } from '@/lib/calc/flooring';

const DEFAULTS: FlooringInputs = {
  areaSqFt: 1000,
  material: 'lvp',
  layout: 'straight',
  needsUnderlayment: true,
};

const MATERIAL_OPTIONS: { value: FlooringMaterial; label: string }[] = [
  { value: 'lvp', label: 'Luxury vinyl plank (LVP)' },
  { value: 'laminate', label: 'Laminate' },
  { value: 'engineered', label: 'Engineered hardwood' },
  { value: 'hardwood', label: 'Solid hardwood' },
  { value: 'tile', label: 'Tile' },
  { value: 'carpet', label: 'Carpet + pad' },
];

export default function FlooringCalc() {
  const [inputs, setInputs] = useState<FlooringInputs>(DEFAULTS);
  const set = <K extends keyof FlooringInputs>(key: K, value: FlooringInputs[K]) =>
    setInputs((prev) => ({ ...prev, [key]: value }));

  const result = useMemo(() => calculateFlooring(inputs), [inputs]);

  const materialLabel =
    MATERIAL_OPTIONS.find((o) => o.value === inputs.material)?.label ?? inputs.material;

  return (
    <CalcSheet
      slug="flooring"
      sheetNo="TO-06"
      sheetTitle="Flooring takeoff"
      calculatorName="Flooring Calculator"
      result={result}
      finePrintBasis="straight-lay waste of 8–10% by material (plus 5 points for diagonal), and typical retail box coverage"
      inputsSummary={[
        { label: 'Floor area', value: `${inputs.areaSqFt} sq ft` },
        { label: 'Material', value: materialLabel },
        { label: 'Layout', value: inputs.layout === 'diagonal' ? 'Diagonal' : 'Straight' },
        { label: 'Underlayment', value: inputs.needsUnderlayment ? 'Needed' : 'Attached pad' },
      ]}
    >
      <NumberField
        label="Floor area"
        unit="ft²"
        value={inputs.areaSqFt}
        onChange={(v) => set('areaSqFt', v)}
        hint="Sum of the rooms getting this floor"
      />
      <SelectField
        label="Material"
        options={MATERIAL_OPTIONS}
        value={inputs.material}
        onChange={(v) => set('material', v)}
      />
      <Seg
        label="Layout"
        options={[{ value: 'straight', label: 'Straight' }, { value: 'diagonal', label: 'Diagonal' }]}
        value={inputs.layout}
        onChange={(v) => set('layout', v as FlooringInputs['layout'])}
        hint="Diagonal and herringbone add 5% waste"
      />
      <Seg
        label="Underlayment"
        options={[{ value: 'yes', label: 'Needed' }, { value: 'no', label: 'Attached pad' }]}
        value={inputs.needsUnderlayment ? 'yes' : 'no'}
        onChange={(v) => set('needsUnderlayment', v === 'yes')}
        hint="Skip if your planks have attached pad; ignored for tile and carpet"
      />
    </CalcSheet>
  );
}
