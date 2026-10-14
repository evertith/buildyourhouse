/**
 * Copy text, CSV, and the inbox payload for an estimate. All three carry
 * the same rows: phase, who does it, cash, hours, and the split.
 */

import type { Estimate } from '@/lib/estimate/estimate';
import { FINISH_LABEL } from '@/lib/estimate/prices';
import { FOUNDATION_LABEL, ROOF_LABEL } from '@/lib/estimate/geometry';
import type { Profile } from '@/lib/estimate/geometry';
import { hoursApprox, money, money100 } from './format';

export const CALCULATOR_SLUG = 'material-estimator';
export const CALCULATOR_NAME = 'Cost to Build a House Calculator';

const mid = (r: { low: number; high: number }) => (r.low + r.high) / 2;

export function profileRows(p: Profile, e: Estimate): { label: string; value: string }[] {
  return [
    { label: 'Finished area', value: `${p.heatedSf.toLocaleString('en-US')} sq ft` },
    { label: 'Stories', value: String(p.stories) },
    { label: 'Finish', value: FINISH_LABEL[p.finish] },
    { label: 'Foundation', value: FOUNDATION_LABEL[p.foundation] },
    { label: 'State', value: e.state.name },
    { label: 'Roof', value: ROOF_LABEL[p.roof] },
    { label: 'Wall height', value: `${p.wallHeightFt} ft` },
    { label: 'Doing yourself', value: e.diy.length ? e.phases.filter((x) => x.diy).map((x) => x.name).join(', ') : 'nothing, every trade hired' },
  ];
}

export function phaseRows(e: Estimate): { label: string; value: string }[] {
  return e.phases.map((p) => {
    const mat = mid(p.materials);
    const lab = mid(p.labor);
    const who = p.soft ? 'paid, not built' : p.diy ? `yourself, about ${hoursApprox(p.hours)} hours` : 'hired';
    const cash = mat + (p.diy ? 0 : lab);
    return { label: p.name, value: `${money100(cash)} (${who})` };
  });
}

export function splitRows(e: Estimate): { label: string; value: string }[] {
  const t = e.totals;
  return [
    { label: 'Materials', value: money100(t.materials.mid) },
    { label: 'Soft costs', value: money100(t.soft.mid) },
    { label: 'Hired labor', value: money100(t.hiredLabor.mid) },
    { label: 'Your hours', value: `${hoursApprox(t.hours)} hours, worth ${money100(t.ownLabor.mid)}` },
    { label: 'Contingency, 10%', value: money100(t.contingency.mid) },
    { label: 'Every trade hired', value: money100(t.allHired.mid) },
  ];
}

export function estimateText(e: Estimate, p: Profile, url: string): string {
  const t = e.totals;
  return [
    `${CALCULATOR_NAME}`,
    url,
    '',
    `Cash to build: ${money100(t.cash.mid)} (likely ${money100(t.cash.low)} to ${money100(t.cash.high)}), about ${money(t.perSqFt.mid)} per sq ft`,
    '',
    'Profile:',
    ...profileRows(p, e).map((r) => `  ${r.label}: ${r.value}`),
    '',
    'Phases:',
    ...phaseRows(e).map((r) => `  ${r.label}: ${r.value}`),
    '',
    ...splitRows(e).map((r) => `${r.label}: ${r.value}`),
    '',
    `Prices are national ranges for ${e.asOf}, scaled to ${e.state.name}. An estimate, not a quote.`,
  ].join('\n');
}

export function estimateCsv(e: Estimate, p: Profile): string {
  const q = (v: string | number) => `"${String(v).replace(/"/g, '""')}"`;
  const rows: (string | number)[][] = [
    ['Phase', 'Who does it', 'Materials low', 'Materials mid', 'Materials high', 'Labor low', 'Labor mid', 'Labor high', 'Hours', 'Cash'],
  ];
  for (const ph of e.phases) {
    const mat = mid(ph.materials);
    const lab = mid(ph.labor);
    rows.push([
      ph.name,
      ph.soft ? 'paid, not built' : ph.diy ? 'yourself' : 'hired',
      Math.round(ph.materials.low),
      Math.round(mat),
      Math.round(ph.materials.high),
      Math.round(ph.labor.low),
      Math.round(lab),
      Math.round(ph.labor.high),
      Math.round(ph.hours),
      Math.round(mat + (ph.diy ? 0 : lab)),
    ]);
  }
  rows.push([]);
  rows.push(['Line items']);
  rows.push(['Phase', 'Item', 'Quantity', 'Unit', 'Detail', 'Cost low', 'Cost high']);
  for (const ph of e.phases) {
    for (const l of ph.lines) {
      rows.push([ph.name, l.label, Math.round(l.qty * 10) / 10, l.unit, l.detail ?? '', Math.round(l.costLow), Math.round(l.costHigh)]);
    }
  }
  rows.push([]);
  rows.push(['Profile']);
  for (const r of profileRows(p, e)) rows.push([r.label, r.value]);
  rows.push([]);
  for (const r of splitRows(e)) rows.push([r.label, r.value]);
  rows.push(['Cash to build', Math.round(e.totals.cash.mid)]);
  rows.push(['Prices', `National ranges, ${e.asOf}, scaled to ${e.state.name}`]);
  return rows.map((r) => r.map(q).join(',')).join('\n');
}

export function csvFilename(p: Profile): string {
  return `cost-to-build-${p.heatedSf}-sqft-${p.state.toLowerCase()}.csv`;
}
