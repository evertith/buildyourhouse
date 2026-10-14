/**
 * The measured rung: StudTally's geometry summary → Geometry → estimate.
 *
 *   node --test --experimental-strip-types src/lib/estimate/__tests__/measured.test.ts
 */

import test from 'node:test';
import assert from 'node:assert/strict';

import { PROFILE_DEFAULTS } from '../geometry.ts';
import { runEstimate } from '../estimate.ts';
import { isMeasured, measuredFacts, measuredGeometry, measuredProfile, planTitle, sheetLabel } from '../measured.ts';
import type { MeasuredPayload } from '../measured.ts';

/** The Thompson set as the partner API summarizes it (decimals as strings). */
const THOMPSON: MeasuredPayload = {
  plan_id: 'p1',
  name: 'Thompson_Final_Set',
  sheets_total: 12,
  sheets_read: 9,
  heated_sf: 2508,
  stories: 1,
  footprint_sf: '2715.0',
  perimeter_lf: '299.0',
  footprint: { width_ft: '81.83', depth_ft: '68.17' },
  wall_height_ft: '10',
  ext_wall_lf: '412.0',
  int_wall_lf: '618.0',
  ext_wall_area_sf: '4120.0',
  openings: { windows: 16, window_area_sf: '262.0', ext_doors: 3, garage_doors: 1 },
  rooms: { count: 24, baths: '3', kitchens: 1, bedrooms: 4 },
  roof: { plane_area_sf: '3140.0', pitch: '8', ridge_lf: '96.0', hip_valley_lf: '58.0', eave_lf: '328.0', framing: 'stick' },
  foundation: 'raised_crawl',
  framed_floor_sf: 2715,
  unheated_sf: 640,
  garage_sf: 520,
  porches: { count: 2, posts: 6 },
  refs: { heated_sf: 'A-1', footprint_sf: 'A-2', ext_wall_lf: 'A-2', openings: 'A-2', rooms: 'A-2', roof: 'A-5', foundation: 'A-1' },
  assumed: ['Roof framing read as stick from sheet A-5.'],
};

test('a full read measures every geometry field it carries', () => {
  const g = measuredGeometry(THOMPSON, PROFILE_DEFAULTS);
  assert.equal(g.heatedSf.value, 2508);
  assert.equal(g.heatedSf.source, 'measured');
  assert.equal(g.heatedSf.ref, 'A-1');
  assert.equal(g.foundation.value, 'crawl');
  assert.equal(g.foundation.source, 'measured');
  assert.equal(g.wallHeightFt.value, 10);
  assert.equal(g.extWallLf.value, 412);
  assert.equal(g.extWallAreaSf.value, 4120);
  assert.equal(g.openings.value.windowAreaSf, 262);
  assert.equal(g.rooms.value.baths, 3);
  assert.equal(g.roof.value.pitch, 8);
  assert.equal(g.roof.value.framing, 'stick');
  assert.equal(g.roof.value.complexity, 'hip');
  assert.equal(g.roof.value.rakeLf, 0);
  assert.equal(g.sides.value.longFt, 81.83);
  assert.equal(g.garageSf.value, 520);
  assert.equal(g.porches.value.posts, 6);
  assert.ok(isMeasured(g));
  assert.deepEqual(g.assumed, THOMPSON.assumed);
});

test('the measured estimate runs and tags nine of fourteen phases measured', () => {
  const g = measuredGeometry(THOMPSON, PROFILE_DEFAULTS);
  const e = runEstimate(g, 'standard', 'NC', { diy: [] });
  const measured = e.phases.filter((p) => p.basis === 'measured').map((p) => p.id);
  assert.deepEqual(measured, [
    'foundation',
    'framing',
    'roofing',
    'openings',
    'exterior',
    'plumbing',
    'insulation',
    'drywallPaint',
    'interior',
  ]);
  assert.ok(e.totals.cash.mid > 250_000 && e.totals.cash.mid < 600_000, `cash ${e.totals.cash.mid}`);
  assert.ok(Number.isFinite(e.totals.perSqFt.mid));
  for (const p of e.phases) {
    for (const l of p.lines) {
      assert.ok(Number.isFinite(l.costLow) && Number.isFinite(l.costHigh), `${p.id}/${l.id}`);
      assert.ok(l.qty >= 0, `${p.id}/${l.id} qty ${l.qty}`);
    }
  }
});

test('a partial read falls back field by field and says so', () => {
  const g = measuredGeometry({ plan_id: 'p2', heated_sf: '1800', stories: 2 }, PROFILE_DEFAULTS);
  assert.equal(g.heatedSf.source, 'measured');
  assert.equal(g.stories.value, 2);
  assert.equal(g.footprintSf.source, 'derived');
  assert.equal(g.footprintSf.value, 900);
  assert.equal(g.roof.source, 'derived');
  assert.equal(g.openings.source, 'derived');
  assert.ok(g.assumed.some((a) => a.startsWith('Roof:')));
  assert.ok(g.assumed.some((a) => a.startsWith('Windows and doors:')));
  const e = runEstimate(g, 'basic', 'TX', {});
  assert.equal(e.phases.filter((p) => p.basis === 'measured').length, 0);
  assert.ok(Number.isFinite(e.totals.cash.mid));
});

test('no garage door on the plan means no garage, whatever the size rule says', () => {
  const g = measuredGeometry(
    { plan_id: 'p3', heated_sf: 2400, openings: { windows: 14, ext_doors: 2, garage_doors: 0 } },
    PROFILE_DEFAULTS
  );
  assert.equal(g.garageSf.value, 0);
  assert.equal(g.unheatedSf.value, 120);
});

test('the profile a read implies keeps the visitor finish and state', () => {
  const p = measuredProfile(THOMPSON, { ...PROFILE_DEFAULTS, finish: 'premium', state: 'GA' });
  assert.equal(p.heatedSf, 2508);
  assert.equal(p.foundation, 'crawl');
  assert.equal(p.wallHeightFt, 10);
  assert.equal(p.roof, 'hip');
  assert.equal(p.finish, 'premium');
  assert.equal(p.state, 'GA');
  const gable = measuredProfile({ plan_id: 'x', roof: { ridge_lf: '60', hip_valley_lf: '0' } }, PROFILE_DEFAULTS);
  assert.equal(gable.roof, 'gable');
  const cutup = measuredProfile({ plan_id: 'x', roof: { ridge_lf: '60', hip_valley_lf: '90' } }, PROFILE_DEFAULTS);
  assert.equal(cutup.roof, 'cutup');
});

test('the facts list names what was read with its sheet', () => {
  const facts = measuredFacts(measuredGeometry(THOMPSON, PROFILE_DEFAULTS));
  assert.ok(facts.length >= 6);
  assert.equal(facts[0].ref, 'A-1');
  assert.match(facts[0].text, /2,508 sq ft heated, one story/);
  assert.match(facts[1].text, /Footprint 81 ft 10 in by 68 ft 2 in/);
  assert.ok(facts.some((f) => /Roof, 31 squares at 8 in 12, stick framed/.test(f.text)));
  assert.ok(facts.some((f) => /Crawl space foundation/.test(f.text)));
});

test('an implausible exterior-door count is priced at the derived count and said so', () => {
  const g = measuredGeometry(
    { plan_id: 'p5', heated_sf: 2508, openings: { windows: 17, ext_doors: 15, garage_doors: 2 } },
    PROFILE_DEFAULTS
  );
  assert.equal(g.openings.source, 'measured');
  assert.equal(g.openings.value.extDoors, 3);
  assert.equal(g.openings.value.windows, 17);
  assert.ok(g.assumed.some((a) => a.startsWith('Exterior doors: the read counted 15')));
});

test('sheet labels and plan titles read as prose', () => {
  assert.equal(sheetLabel('A-2'), 'sheet A-2');
  assert.equal(sheetLabel('3'), 'sheet 3');
  assert.equal(sheetLabel('sheet 3'), 'sheet 3');
  assert.equal(planTitle('Thompson_Final_Set'), 'Thompson Final Set, costed.');
  assert.equal(planTitle('2589-S_Thompson_-_Final_Set_09_23_21'), 'Your plans, costed.');
  assert.equal(planTitle(undefined), 'Your plans, costed.');
});
