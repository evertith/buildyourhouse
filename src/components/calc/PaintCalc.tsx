'use client';

import { useMemo, useState } from 'react';
import CalcSheet, { BarRow } from './CalcSheet';
import { DimPair, NumberField, Seg } from './fields';
import { calculatePaint, PaintInputs } from '@/lib/calc/paint';

const DEFAULTS: PaintInputs = {
  mode: 'room',
  roomLengthFt: 12,
  roomWidthFt: 12,
  ceilingHeightFt: 8,
  doors: 1,
  windows: 2,
  floorAreaSqFt: 2000,
  coats: 2,
  includeCeilings: true,
  includeTrim: true,
  newDrywall: false,
};

export default function PaintCalc() {
  const [inputs, setInputs] = useState<PaintInputs>(DEFAULTS);
  const set = <K extends keyof PaintInputs>(key: K, value: PaintInputs[K]) =>
    setInputs((prev) => ({ ...prev, [key]: value }));

  const result = useMemo(() => calculatePaint(inputs), [inputs]);

  // Gallon-share breakdown — comparable across lines priced in different
  // products (latex vs. primer vs. enamel), using cost-range midpoints.
  const bars: BarRow[] = result.lines.map((l) => ({
    key: l.id,
    label: l.label.replace('Wall paint', 'Walls').replace('Ceiling paint', 'Ceilings').replace('Drywall primer', 'Primer').replace('Trim enamel', 'Trim'),
    qty: ((l.costLow ?? 0) + (l.costHigh ?? 0)) / 2,
    valueLabel: `${l.qty} gal`,
  }));

  const inputsSummary =
    inputs.mode === 'room'
      ? [
          { label: 'Mode', value: 'One room' },
          { label: 'Room size', value: `${inputs.roomLengthFt} × ${inputs.roomWidthFt} ft` },
          { label: 'Ceiling height', value: `${inputs.ceilingHeightFt} ft` },
          { label: 'Doors', value: String(inputs.doors) },
          { label: 'Windows', value: String(inputs.windows) },
          { label: 'Coats', value: String(inputs.coats) },
          { label: 'Ceilings', value: inputs.includeCeilings ? 'Included' : 'Skipped' },
          { label: 'Trim', value: inputs.includeTrim ? 'Included' : 'Skipped' },
          { label: 'Surface', value: inputs.newDrywall ? 'New drywall' : 'Repaint' },
        ]
      : [
          { label: 'Mode', value: 'Whole house' },
          { label: 'Floor area', value: `${inputs.floorAreaSqFt} sq ft` },
          { label: 'Coats', value: String(inputs.coats) },
          { label: 'Ceilings', value: inputs.includeCeilings ? 'Included' : 'Skipped' },
          { label: 'Trim', value: inputs.includeTrim ? 'Included' : 'Skipped' },
          { label: 'Surface', value: inputs.newDrywall ? 'New drywall' : 'Repaint' },
        ];

  return (
    <CalcSheet
      slug="paint"
      sheetNo="TO-05"
      sheetTitle="Paint takeoff"
      calculatorName="Paint Calculator"
      result={result}
      bars={bars}
      barsLabel="Where the gallons go"
      finePrintBasis="350 sq ft per gallon per coat on smooth drywall, with 21 sq ft per door and 15 per window deducted"
      inputsSummary={inputsSummary}
    >
      <Seg
        label="Mode"
        options={[{ value: 'room', label: 'One room' }, { value: 'house', label: 'Whole house' }]}
        value={inputs.mode}
        onChange={(v) => set('mode', v as PaintInputs['mode'])}
      />
      {inputs.mode === 'room' ? (
        <>
          <DimPair
            label="Room size"
            lengthValue={inputs.roomLengthFt}
            widthValue={inputs.roomWidthFt}
            onLength={(v) => set('roomLengthFt', v)}
            onWidth={(v) => set('roomWidthFt', v)}
            hint="Wall to wall, in feet"
          />
          <Seg
            label="Ceiling height"
            options={[{ value: 8, label: '8 ft' }, { value: 9, label: '9 ft' }, { value: 10, label: '10 ft' }]}
            value={inputs.ceilingHeightFt}
            onChange={(v) => set('ceilingHeightFt', v)}
          />
          <NumberField
            label="Doors"
            unit="doors"
            value={inputs.doors}
            onChange={(v) => set('doors', v)}
            hint="21 sq ft deducted each"
            step={1}
          />
          <NumberField
            label="Windows"
            unit="windows"
            value={inputs.windows}
            onChange={(v) => set('windows', v)}
            hint="15 sq ft deducted each"
            step={1}
          />
        </>
      ) : (
        <NumberField
          label="Floor area"
          unit="ft²"
          value={inputs.floorAreaSqFt}
          onChange={(v) => set('floorAreaSqFt', v)}
          hint="Finished square footage getting paint"
        />
      )}
      <Seg
        label="Coats"
        options={[{ value: 1, label: '1' }, { value: 2, label: '2' }]}
        value={inputs.coats}
        onChange={(v) => set('coats', v as PaintInputs['coats'])}
        hint="Two coats is the honest default for color changes and new drywall"
      />
      <Seg
        label="Ceilings"
        options={[{ value: 'yes', label: 'Included' }, { value: 'no', label: 'Skip' }]}
        value={inputs.includeCeilings ? 'yes' : 'no'}
        onChange={(v) => set('includeCeilings', v === 'yes')}
      />
      <Seg
        label="Trim"
        options={[{ value: 'yes', label: 'Included' }, { value: 'no', label: 'Skip' }]}
        value={inputs.includeTrim ? 'yes' : 'no'}
        onChange={(v) => set('includeTrim', v === 'yes')}
      />
      <Seg
        label="Surface"
        options={[{ value: 'new', label: 'New drywall' }, { value: 'repaint', label: 'Repaint' }]}
        value={inputs.newDrywall ? 'new' : 'repaint'}
        onChange={(v) => set('newDrywall', v === 'new')}
        hint="New board needs PVA primer"
      />
    </CalcSheet>
  );
}
