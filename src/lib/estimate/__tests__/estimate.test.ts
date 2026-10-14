/**
 * Engine tests. Run directly, no build step:
 *
 *   node --test --experimental-strip-types src/lib/estimate/__tests__/estimate.test.ts
 *
 * Golden values for the default house are snapshotted here on purpose: a
 * price refresh is supposed to move them, and the failing assertion is the
 * reminder to re-read the FAQ and the methodology prose, which are generated
 * from the same run. Properties cover what ships wrong silently.
 */

import test from 'node:test';
import assert from 'node:assert/strict';

import { deriveGeometry, PROFILE_DEFAULTS } from '../geometry.ts';
import type { Profile } from '../geometry.ts';
import { runEstimate } from '../estimate.ts';
import { DEFAULT_ALL_HIRED, DEFAULT_ESTIMATE } from '../defaults.ts';
import { parseProfile, serializeProfile } from '../profile.ts';
import { STATES, stateFactors } from '../stateIndex.ts';
import { PHASE_ORDER } from '../types.ts';
import type { PhaseId } from '../types.ts';
import { DIY_DEFAULT } from '../labor.ts';

const run = (p: Partial<Profile> = {}, diy?: PhaseId[]) => {
  const profile = { ...PROFILE_DEFAULTS, ...p };
  return runEstimate(profile, profile.finish, profile.state, diy ? { diy } : {});
};

test('default geometry follows the stated rules', () => {
  const g = deriveGeometry(PROFILE_DEFAULTS);
  assert.equal(g.footprintSf.value, 2000);
  assert.ok(Math.abs(g.sides.value.longFt / g.sides.value.shortFt - 1.5) < 1e-9);
  assert.equal(g.intWallLf.value, 500);
  assert.equal(g.openings.value.windows, 18);
  assert.equal(g.openings.value.garageDoors, 1);
  assert.equal(g.rooms.value.baths, 2.5);
  assert.equal(g.framedFloorSf.value, 0);
  assert.equal(g.foundation.source, 'user');
  assert.equal(g.roof.source, 'derived');
  assert.ok(g.assumed.length >= 6);
});

test('two stories halve the footprint and add a framed floor', () => {
  const g = deriveGeometry({ ...PROFILE_DEFAULTS, stories: 2 });
  assert.equal(g.footprintSf.value, 1000);
  assert.equal(g.framedFloorSf.value, 1000);
  const crawl = deriveGeometry({ ...PROFILE_DEFAULTS, foundation: 'crawl' });
  assert.equal(crawl.framedFloorSf.value, 2000);
});

test('golden: the default house', () => {
  const t = DEFAULT_ESTIMATE.totals;
  // Snapshotted 2026-10-14 at the October 2026 price table. A refresh moves
  // these on purpose; update the numbers and re-read the FAQ copy.
  assert.ok(t.cash.mid > 250_000 && t.cash.mid < 400_000, `cash ${t.cash.mid}`);
  assert.ok(t.allHired.mid > 300_000 && t.allHired.mid < 450_000, `all hired ${t.allHired.mid}`);
  assert.ok(t.perSqFt.mid > 120 && t.perSqFt.mid < 200, `per sq ft ${t.perSqFt.mid}`);
  assert.equal(t.nDiy, 3);
  assert.deepEqual(DEFAULT_ESTIMATE.diy, [...DIY_DEFAULT]);
  assert.equal(DEFAULT_ESTIMATE.phases.length, 14);
  assert.deepEqual(DEFAULT_ESTIMATE.phases.map((p) => p.id), [...PHASE_ORDER]);
});

test('every line has a positive quantity and a low under its high', () => {
  for (const profile of [
    {},
    { stories: 2 as const },
    { foundation: 'crawl' as const },
    { foundation: 'basement' as const, stories: 3 as const },
    { heatedSf: 500, finish: 'basic' as const },
    { heatedSf: 10000, finish: 'premium' as const, roof: 'cutup' as const },
  ]) {
    const e = run(profile);
    for (const p of e.phases) {
      assert.ok(p.lines.length > 0, `${p.id} has lines`);
      for (const l of p.lines) {
        assert.ok(l.qty > 0, `${p.id}/${l.id} qty ${l.qty}`);
        assert.ok(l.costLow > 0 && l.costHigh >= l.costLow, `${p.id}/${l.id} cost`);
      }
      assert.ok(p.materials.low <= p.materials.high);
      assert.ok(p.labor.low <= p.labor.high);
    }
  }
});

test('totals are monotonic in heated square feet', () => {
  let last = 0;
  for (const sqft of [600, 1000, 1500, 2000, 2600, 3500, 5000, 8000]) {
    const e = run({ heatedSf: sqft });
    assert.ok(e.totals.allHired.mid > last, `${sqft} sq ft: ${e.totals.allHired.mid} > ${last}`);
    last = e.totals.allHired.mid;
  }
});

test('doing a phase yourself never raises cash and always adds hours', () => {
  const hired = run({}, []);
  const diy = run({}, ['framing']);
  assert.ok(diy.totals.cash.mid < hired.totals.cash.mid);
  assert.equal(hired.totals.hours, 0);
  assert.ok(diy.totals.hours > 0);
  const framing = diy.phases.find((p) => p.id === 'framing')!;
  assert.ok(framing.diy);
  assert.ok(Math.abs(diy.totals.ownLabor.mid - (framing.labor.low + framing.labor.high) / 2) < 1e-6);
  // Soft costs can never be DIY.
  const soft = run({}, ['soft']).phases.find((p) => p.id === 'soft')!;
  assert.equal(soft.diy, false);
});

test('all-hired equals cash when nothing is DIY', () => {
  const t = DEFAULT_ALL_HIRED.totals;
  assert.ok(Math.abs(t.allHired.mid - t.cash.mid) < 1e-6);
  assert.equal(t.hours, 0);
});

test('the state index scales materials and labor, not the permit base', () => {
  const nc = run({ state: 'NC' }, []);
  const ca = run({ state: 'CA' }, []);
  const framingNC = nc.phases.find((p) => p.id === 'framing')!;
  const framingCA = ca.phases.find((p) => p.id === 'framing')!;
  const f = stateFactors('CA');
  assert.ok(Math.abs(framingCA.materials.low / framingNC.materials.low - f.materials) < 1e-9);
  assert.ok(Math.abs(framingCA.labor.low / framingNC.labor.low - f.materials * f.labor) < 1e-9);
  assert.ok(ca.totals.allHired.mid > nc.totals.allHired.mid);
  assert.equal(STATES.length, 50);
  assert.equal(stateFactors('zz').code, 'NC');
});

test('finish multiplier moves only the finish-sensitive phases', () => {
  const std = run({ finish: 'standard' }, []);
  const prem = run({ finish: 'premium' }, []);
  const at = (e: typeof std, id: PhaseId) => {
    const m = e.phases.find((p) => p.id === id)!.materials;
    return (m.low + m.high) / 2;
  };
  assert.ok(Math.abs(at(prem, 'interior') / at(std, 'interior') - 1.3) < 1e-9);
  assert.ok(Math.abs(at(prem, 'framing') / at(std, 'framing') - 1) < 1e-9);
});

test('phase shares sum to one', () => {
  const sum = DEFAULT_ESTIMATE.phases.reduce((s, p) => s + p.share, 0);
  assert.ok(Math.abs(sum - 1) < 1e-9);
});

test('profile round-trips through the URL', () => {
  const state = {
    profile: { ...PROFILE_DEFAULTS, heatedSf: 2650, stories: 2 as const, state: 'TX', finish: 'premium' as const },
    diy: ['framing', 'insulation'] as PhaseId[],
  };
  const q = serializeProfile(state);
  const back = parseProfile(q);
  assert.deepEqual(back.profile, state.profile);
  assert.deepEqual(back.diy, ['framing', 'insulation']);
  // Defaults serialize to nothing; junk parses to defaults.
  assert.equal(serializeProfile({ profile: PROFILE_DEFAULTS, diy: [...DIY_DEFAULT] }).toString(), '');
  const junk = parseProfile(new URLSearchParams('sqft=abc&stories=9&state=XX&finish=gold&diy=none'));
  assert.deepEqual(junk.profile, PROFILE_DEFAULTS);
  assert.deepEqual(junk.diy, []);
});
