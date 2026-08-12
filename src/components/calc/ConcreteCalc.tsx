'use client';

import { useMemo, useState } from 'react';
import CalcSheet from './CalcSheet';
import { DimPair, Seg } from './fields';
import { calculateConcrete, ConcreteInputs } from '@/lib/calc/concrete';

const DEFAULTS: ConcreteInputs = {
  lengthFt: 24,
  widthFt: 24,
  thicknessIn: 4,
  thickenedEdge: true,
  reinforcement: 'mesh',
};

const REINFORCEMENT_LABEL: Record<ConcreteInputs['reinforcement'], string> = {
  none: 'None',
  mesh: 'Wire mesh',
  rebar: '#4 rebar',
};

export default function ConcreteCalc() {
  const [inputs, setInputs] = useState<ConcreteInputs>(DEFAULTS);
  const set = <K extends keyof ConcreteInputs>(key: K, value: ConcreteInputs[K]) =>
    setInputs((prev) => ({ ...prev, [key]: value }));

  const result = useMemo(() => calculateConcrete(inputs), [inputs]);

  return (
    <CalcSheet
      slug="concrete-slab"
      sheetNo="TO-03"
      sheetTitle="Concrete takeoff"
      calculatorName="Concrete Slab Calculator"
      result={result}
      finePrintBasis="a rectangular slab at the chosen thickness, a 10% order margin, and quarter-yard rounding"
      inputsSummary={[
        { label: 'Slab dimensions', value: `${inputs.lengthFt} × ${inputs.widthFt} ft` },
        { label: 'Thickness', value: `${inputs.thicknessIn}"` },
        { label: 'Thickened edge', value: inputs.thickenedEdge ? 'Yes' : 'No' },
        { label: 'Reinforcement', value: REINFORCEMENT_LABEL[inputs.reinforcement] },
      ]}
    >
      <DimPair
        label="Slab dimensions"
        lengthValue={inputs.lengthFt}
        widthValue={inputs.widthFt}
        onLength={(v) => set('lengthFt', v)}
        onWidth={(v) => set('widthFt', v)}
        hint="Slab edge to slab edge"
      />
      <Seg
        label="Thickness"
        options={[{ value: 4, label: '4"' }, { value: 5, label: '5"' }, { value: 6, label: '6"' }]}
        value={inputs.thicknessIn}
        onChange={(v) => set('thicknessIn', v as ConcreteInputs['thicknessIn'])}
      />
      <Seg
        label="Thickened edge"
        options={[{ value: 'yes', label: 'Yes' }, { value: 'no', label: 'No' }]}
        value={inputs.thickenedEdge ? 'yes' : 'no'}
        onChange={(v) => set('thickenedEdge', v === 'yes')}
        hint='Monolithic garage and shed slabs pour a 12×12" footing around the perimeter'
      />
      <Seg
        label="Reinforcement"
        options={[
          { value: 'none', label: 'None' },
          { value: 'mesh', label: 'Mesh' },
          { value: 'rebar', label: 'Rebar' },
        ]}
        value={inputs.reinforcement}
        onChange={(v) => set('reinforcement', v as ConcreteInputs['reinforcement'])}
        hint='Rebar is figured as #4 both ways at 24" OC'
      />
    </CalcSheet>
  );
}
