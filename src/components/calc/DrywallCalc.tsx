'use client';

import { useMemo, useState } from 'react';
import CalcSheet from './CalcSheet';
import { DimPair, NumberField, Seg } from './fields';
import { calculateDrywall, DrywallInputs } from '@/lib/calc/drywall';

const DEFAULTS: DrywallInputs = {
  mode: 'house',
  floorAreaSqFt: 2000,
  sheetSize: '4x8',
  roomLengthFt: 12,
  roomWidthFt: 12,
  ceilingHeightFt: 8,
  includeCeiling: true,
};

export default function DrywallCalc() {
  const [inputs, setInputs] = useState<DrywallInputs>(DEFAULTS);
  const set = <K extends keyof DrywallInputs>(key: K, value: DrywallInputs[K]) =>
    setInputs((prev) => ({ ...prev, [key]: value }));

  const result = useMemo(() => calculateDrywall(inputs), [inputs]);

  // No breakdown bars: sheets dominate this takeoff, and a one-bar chart is
  // noise (design spec §4.6 — bars only when components are meaningful).

  const isHouse = inputs.mode === 'house';

  const inputsSummary = isHouse
    ? [
        { label: 'Mode', value: 'Whole house' },
        { label: 'Floor area', value: `${inputs.floorAreaSqFt.toLocaleString('en-US')} sq ft` },
        { label: 'Sheet size', value: inputs.sheetSize === '4x8' ? '4×8' : '4×12' },
      ]
    : [
        { label: 'Mode', value: 'One room' },
        { label: 'Room', value: `${inputs.roomLengthFt} × ${inputs.roomWidthFt} ft` },
        { label: 'Ceiling height', value: `${inputs.ceilingHeightFt} ft` },
        { label: 'Ceiling', value: inputs.includeCeiling ? 'Included' : 'Walls only' },
        { label: 'Sheet size', value: inputs.sheetSize === '4x8' ? '4×8' : '4×12' },
      ];

  return (
    <CalcSheet
      slug="drywall"
      sheetNo="TO-02"
      sheetTitle="Drywall takeoff"
      calculatorName="Drywall Calculator"
      result={result}
      finePrintBasis={
        isHouse
          ? 'the 3.7 × floor-area whole-house heuristic with 10% cut waste'
          : 'perimeter × height walls with a 10% openings allowance and 10% cut waste'
      }
      inputsSummary={inputsSummary}
    >
      <Seg
        label="Mode"
        options={[{ value: 'house', label: 'Whole house' }, { value: 'room', label: 'One room' }]}
        value={inputs.mode}
        onChange={(v) => set('mode', v as DrywallInputs['mode'])}
        hint="House mode is a planning heuristic; room mode is a real takeoff"
      />
      {isHouse ? (
        <NumberField
          label="Floor area"
          unit="ft²"
          value={inputs.floorAreaSqFt}
          onChange={(v) => set('floorAreaSqFt', v)}
          hint="Total finished floor area, all stories"
        />
      ) : (
        <>
          <DimPair
            label="Room dimensions"
            lengthValue={inputs.roomLengthFt}
            widthValue={inputs.roomWidthFt}
            onLength={(v) => set('roomLengthFt', v)}
            onWidth={(v) => set('roomWidthFt', v)}
            hint="Wall to wall, inside the room"
          />
          <Seg
            label="Ceiling height"
            options={[{ value: 8, label: '8 ft' }, { value: 9, label: '9 ft' }, { value: 10, label: '10 ft' }]}
            value={inputs.ceilingHeightFt}
            onChange={(v) => set('ceilingHeightFt', v)}
          />
          <Seg
            label="Ceiling"
            options={[{ value: 'yes', label: 'Included' }, { value: 'no', label: 'Walls only' }]}
            value={inputs.includeCeiling ? 'yes' : 'no'}
            onChange={(v) => set('includeCeiling', v === 'yes')}
            hint="Included adds length × width to the board area"
          />
        </>
      )}
      <Seg
        label="Sheet size"
        options={[{ value: '4x8', label: '4×8' }, { value: '4x12', label: '4×12' }]}
        value={inputs.sheetSize}
        onChange={(v) => set('sheetSize', v as DrywallInputs['sheetSize'])}
        hint='4×12 means fewer butt joints; a 1/2" sheet runs near 80 lb'
      />
    </CalcSheet>
  );
}
