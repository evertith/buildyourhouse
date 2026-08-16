'use client';

import { useMemo, useState } from 'react';
import CalcSheet, { BarRow } from './CalcSheet';
import { NumberField } from './fields';
import { formatCurrency } from '@/lib/calc/format';
import { calculateCostSavings, CostSavingsInputs } from '@/lib/calc/costSavings';

const DEFAULTS: CostSavingsInputs = {
  homeSize: 2000,
  estimatedCost: 300000,
  gcFeePercentage: 14,
  laborHours: 500,
  hourlyWage: 30,
};

export default function CostSavingsCalc() {
  const [inputs, setInputs] = useState<CostSavingsInputs>(DEFAULTS);
  const set = <K extends keyof CostSavingsInputs>(key: K, value: CostSavingsInputs[K]) =>
    setInputs((prev) => ({ ...prev, [key]: value }));

  const result = useMemo(() => calculateCostSavings(inputs), [inputs]);

  // Two checkbooks side by side, plus the sweat equity that is not in either.
  const bars: BarRow[] = [
    {
      key: 'gc',
      label: 'With a GC',
      qty: result.contractPrice,
      valueLabel: formatCurrency(result.contractPrice),
    },
    {
      key: 'self',
      label: 'You as GC',
      qty: result.netProjectCost,
      valueLabel: formatCurrency(result.netProjectCost),
    },
    {
      key: 'sweat',
      label: 'Your hours',
      qty: result.laborValueSavings,
      valueLabel: `${formatCurrency(result.laborValueSavings)} · not cash`,
    },
  ];

  return (
    <CalcSheet
      slug="cost-savings-calculator"
      sheetNo="W-01"
      sheetTitle="Savings worksheet"
      calculatorName="Owner-Builder Cost Savings Calculator"
      inputsLabel="Project figures"
      result={result}
      bars={bars}
      barsLabel="What you write checks for"
      finePrintBasis="a builder’s fee quoted as a percentage of the total contract price, and a budget that already pays subcontractors and suppliers at market rates"
      inputsSummary={[
        { label: 'Build cost with a GC', value: formatCurrency(inputs.estimatedCost) },
        { label: 'Home size', value: `${inputs.homeSize} sq ft` },
        { label: 'GC fee', value: `${inputs.gcFeePercentage}%` },
        { label: 'Hours you put in', value: `${inputs.laborHours} hrs` },
        { label: 'Value of your time', value: `$${inputs.hourlyWage}/hr` },
      ]}
    >
      <NumberField
        label="Build cost with a GC"
        unit="$"
        value={inputs.estimatedCost}
        onChange={(v) => set('estimatedCost', v)}
        step={10000}
        hint="The all-in price a general contractor would quote — materials, subs, and their fee"
      />
      <NumberField
        label="Home size"
        unit="sq ft"
        value={inputs.homeSize}
        onChange={(v) => set('homeSize', v)}
        step={100}
        hint="Finished, conditioned square footage"
      />
      <NumberField
        label="GC fee in your market"
        unit="%"
        value={inputs.gcFeePercentage}
        onChange={(v) => set('gcFeePercentage', v)}
        step={1}
        hint="15–20% is typical; hot markets run higher. Capped at 30%."
      />
      <NumberField
        label="Hours you’ll work yourself"
        unit="hrs"
        value={inputs.laborHours}
        onChange={(v) => set('laborHours', v)}
        step={50}
        hint="Managing plus building. Typical owner-builder: 400–1,000 hours."
      />
      <NumberField
        label="Value of your time"
        unit="$/hr"
        value={inputs.hourlyWage}
        onChange={(v) => set('hourlyWage', v)}
        step={5}
        hint="What you’d earn elsewhere in that hour, or what the free time is worth to you"
      />
    </CalcSheet>
  );
}
