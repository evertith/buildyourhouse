'use client';

import { useMemo, useState } from 'react';
import CalcSheet from './CalcSheet';
import { DimPair, NumberField, Seg } from './fields';
import { calculateInsulation, InsulationInputs } from '@/lib/calc/insulation';

const DEFAULTS: InsulationInputs = {
  scope: 'both',
  wallInput: 'footprint',
  lengthFt: 40,
  widthFt: 30,
  stories: 1,
  wallHeightFt: 8,
  wallAreaSqFt: 1000,
  wallR: 'r13',
  atticAreaSqFt: 1200,
  atticR: 'r38',
};

const WALL_R_LABEL: Record<InsulationInputs['wallR'], string> = {
  r13: 'R-13',
  r15: 'R-15',
  r19: 'R-19',
  r21: 'R-21',
};

const ATTIC_R_LABEL: Record<InsulationInputs['atticR'], string> = {
  r38: 'R-38',
  r49: 'R-49',
};

export default function InsulationCalc() {
  const [inputs, setInputs] = useState<InsulationInputs>(DEFAULTS);
  const set = <K extends keyof InsulationInputs>(key: K, value: InsulationInputs[K]) =>
    setInputs((prev) => ({ ...prev, [key]: value }));

  const result = useMemo(() => calculateInsulation(inputs), [inputs]);

  const inputsSummary: { label: string; value: string }[] = [
    {
      label: 'Scope',
      value:
        inputs.scope === 'both' ? 'Walls + attic' : inputs.scope === 'walls' ? 'Walls only' : 'Attic only',
    },
  ];
  if (inputs.scope !== 'attic') {
    if (inputs.wallInput === 'footprint') {
      inputsSummary.push(
        { label: 'Footprint', value: `${inputs.lengthFt} × ${inputs.widthFt} ft` },
        { label: 'Stories', value: String(inputs.stories) },
        { label: 'Wall height', value: `${inputs.wallHeightFt} ft` }
      );
    } else {
      inputsSummary.push({ label: 'Wall area', value: `${inputs.wallAreaSqFt} sq ft` });
    }
    inputsSummary.push({ label: 'Wall insulation', value: `${WALL_R_LABEL[inputs.wallR]} batts` });
  }
  if (inputs.scope !== 'walls') {
    inputsSummary.push(
      { label: 'Attic area', value: `${inputs.atticAreaSqFt} sq ft` },
      { label: 'Attic insulation', value: `Blown-in to ${ATTIC_R_LABEL[inputs.atticR]}` }
    );
  }

  return (
    <CalcSheet
      slug="insulation"
      sheetNo="TO-07"
      sheetTitle="Insulation takeoff"
      calculatorName="Insulation Calculator"
      result={result}
      finePrintBasis={
        inputs.scope !== 'attic' && inputs.wallInput === 'footprint'
          ? 'manufacturer bag-chart coverage (rounded), a 15% wall-openings deduction, and a 5% cut allowance'
          : 'manufacturer bag-chart coverage (rounded) and a 5% cut allowance'
      }
      inputsSummary={inputsSummary}
    >
      <Seg
        label="Scope"
        options={[
          { value: 'both', label: 'Walls + attic' },
          { value: 'walls', label: 'Walls only' },
          { value: 'attic', label: 'Attic only' },
        ]}
        value={inputs.scope}
        onChange={(v) => set('scope', v as InsulationInputs['scope'])}
      />
      {inputs.scope !== 'attic' && (
        <>
          <Seg
            label="Wall input"
            options={[
              { value: 'footprint', label: 'From footprint' },
              { value: 'area', label: 'Wall area' },
            ]}
            value={inputs.wallInput}
            onChange={(v) => set('wallInput', v as InsulationInputs['wallInput'])}
          />
          {inputs.wallInput === 'footprint' ? (
            <>
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
                onChange={(v) => set('stories', v as InsulationInputs['stories'])}
              />
              <Seg
                label="Wall height"
                options={[{ value: 8, label: '8 ft' }, { value: 9, label: '9 ft' }, { value: 10, label: '10 ft' }]}
                value={inputs.wallHeightFt}
                onChange={(v) => set('wallHeightFt', v as InsulationInputs['wallHeightFt'])}
              />
            </>
          ) : (
            <NumberField
              label="Wall area"
              unit="ft²"
              value={inputs.wallAreaSqFt}
              onChange={(v) => set('wallAreaSqFt', v)}
              hint="Net cavity area — subtract windows and doors yourself"
            />
          )}
          <Seg
            label="Wall R-value"
            options={[
              { value: 'r13', label: 'R-13' },
              { value: 'r15', label: 'R-15' },
              { value: 'r19', label: 'R-19' },
              { value: 'r21', label: 'R-21' },
            ]}
            value={inputs.wallR}
            onChange={(v) => set('wallR', v as InsulationInputs['wallR'])}
            hint="R-13/15 fit 2×4 walls; R-19/21 need 2×6"
          />
        </>
      )}
      {inputs.scope !== 'walls' && (
        <>
          <NumberField
            label="Attic area"
            unit="ft²"
            value={inputs.atticAreaSqFt}
            onChange={(v) => set('atticAreaSqFt', v)}
            hint="Flat ceiling area, not roof area"
          />
          <Seg
            label="Attic R-value"
            options={[
              { value: 'r38', label: 'R-38' },
              { value: 'r49', label: 'R-49' },
            ]}
            value={inputs.atticR}
            onChange={(v) => set('atticR', v as InsulationInputs['atticR'])}
            hint="Colder zones need R-49; check the guide below"
          />
        </>
      )}
    </CalcSheet>
  );
}
