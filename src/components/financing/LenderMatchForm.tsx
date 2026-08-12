'use client';

/**
 * Owner-builder lender-match intake — the qualified-lead form. Field set
 * matches the qualified-lead definition in lender-outreach/pricing-sheet.md
 * §2 exactly (name, email, phone, state, timeline, credit band, land
 * status), plus optional budget band and notes.
 *
 * Fires generate_lead { method: 'financing_form', state } on confirmed
 * success only. Never promises a specific lender — the honest offer is a
 * personal pointer toward lenders that fit the project.
 */

import { FormEvent, useState } from 'react';
import s from '@/styles/Financing.module.css';
import { trackEvent } from '@/lib/analytics';

const WORKER_BASE =
  process.env.NEXT_PUBLIC_NEWSLETTER_WORKER_BASE ??
  'https://buildyourhouse-newsletter.azerothcorner.workers.dev';

const STATES = [
  'AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN',
  'IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH',
  'NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT',
  'VT','VA','WA','WV','WI','WY',
];

export default function LenderMatchForm() {
  const [form, setForm] = useState({
    name: '',
    email: '',
    phone: '',
    state: '',
    timeline: '',
    creditBand: '',
    landStatus: '',
    budgetBand: '',
    notes: '',
  });
  const [honeypot, setHoneypot] = useState('');
  const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle');

  const set = (key: keyof typeof form) => (value: string) =>
    setForm((prev) => ({ ...prev, [key]: value }));

  const submit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (status === 'loading') return;
    setStatus('loading');
    try {
      const res = await fetch(`${WORKER_BASE}/financing-lead`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          ...form,
          website: honeypot,
          sourcePath: window.location.pathname,
        }),
      });
      if (!res.ok) throw new Error(`lead submit failed: ${res.status}`);
      setStatus('success');
      trackEvent('generate_lead', { method: 'financing_form', state: form.state });
    } catch {
      setStatus('error');
    }
  };

  if (status === 'success') {
    return (
      <div className={s.form} id="lender-match">
        <p className={s.done} role="status">
          Got it — thanks. I&apos;ll look at your project and reply within a couple of
          business days with lenders worth calling for your state and situation.
          Nothing is submitted to any lender until you decide to apply.
        </p>
      </div>
    );
  }

  return (
    <div className={s.form} id="lender-match">
      <p className={s.formHead}>Get pointed at the right lender</p>
      <p className={s.formSub}>
        Tell me about your project and I&apos;ll reply with the lenders most likely to
        say yes to it — matched to your state, timeline, and land situation. Free,
        no obligation, and your details go nowhere without your say-so.
      </p>
      <form className={s.grid} onSubmit={submit}>
        {/* Honeypot — hidden from real users, bots auto-fill it */}
        <input
          type="text"
          name="website"
          value={honeypot}
          onChange={(e) => setHoneypot(e.target.value)}
          style={{ position: 'absolute', left: '-9999px', height: 0, width: 0, opacity: 0 }}
          tabIndex={-1}
          autoComplete="off"
          aria-hidden="true"
        />

        <div className={s.field}>
          <label className={s.label} htmlFor="fl-name">Name</label>
          <input id="fl-name" className={s.input} required maxLength={80}
            value={form.name} onChange={(e) => set('name')(e.target.value)} />
        </div>
        <div className={s.field}>
          <label className={s.label} htmlFor="fl-email">Email</label>
          <input id="fl-email" className={s.input} type="email" required
            value={form.email} onChange={(e) => set('email')(e.target.value)} />
        </div>
        <div className={s.field}>
          <label className={s.label} htmlFor="fl-phone">Phone</label>
          <input id="fl-phone" className={s.input} type="tel" required
            placeholder="(555) 555-0100"
            value={form.phone} onChange={(e) => set('phone')(e.target.value)} />
        </div>
        <div className={s.field}>
          <label className={s.label} htmlFor="fl-state">Build state</label>
          <div className={s.selectWrap}>
            <select id="fl-state" className={s.select} required
              value={form.state} onChange={(e) => set('state')(e.target.value)}>
              <option value="" disabled>Select state</option>
              {STATES.map((st) => <option key={st} value={st}>{st}</option>)}
            </select>
          </div>
        </div>
        <div className={s.field}>
          <label className={s.label} htmlFor="fl-timeline">When do you plan to break ground?</label>
          <div className={s.selectWrap}>
            <select id="fl-timeline" className={s.select} required
              value={form.timeline} onChange={(e) => set('timeline')(e.target.value)}>
              <option value="" disabled>Select timeline</option>
              <option value="0-6">Within 6 months</option>
              <option value="6-12">6–12 months</option>
              <option value="12-18">12–18 months</option>
              <option value="18plus">18+ months</option>
            </select>
          </div>
        </div>
        <div className={s.field}>
          <label className={s.label} htmlFor="fl-credit">Credit score range</label>
          <div className={s.selectWrap}>
            <select id="fl-credit" className={s.select} required
              value={form.creditBand} onChange={(e) => set('creditBand')(e.target.value)}>
              <option value="" disabled>Select range</option>
              <option value="740plus">740+</option>
              <option value="700-739">700–739</option>
              <option value="660-699">660–699</option>
              <option value="below-660">Below 660</option>
              <option value="unsure">Not sure</option>
            </select>
          </div>
        </div>
        <div className={s.field}>
          <label className={s.label} htmlFor="fl-land">Land status</label>
          <div className={s.selectWrap}>
            <select id="fl-land" className={s.select} required
              value={form.landStatus} onChange={(e) => set('landStatus')(e.target.value)}>
              <option value="" disabled>Select status</option>
              <option value="own">I own the land</option>
              <option value="under-contract">Under contract</option>
              <option value="looking">Still looking</option>
            </select>
          </div>
        </div>
        <div className={s.field}>
          <label className={s.label} htmlFor="fl-budget">Construction budget (optional)</label>
          <div className={s.selectWrap}>
            <select id="fl-budget" className={s.select}
              value={form.budgetBand} onChange={(e) => set('budgetBand')(e.target.value)}>
              <option value="">Prefer not to say</option>
              <option value="under-200k">Under $200K</option>
              <option value="200-400k">$200–400K</option>
              <option value="400-700k">$400–700K</option>
              <option value="over-700k">$700K+</option>
            </select>
          </div>
        </div>
        <div className={`${s.field} ${s.fieldWide}`}>
          <label className={s.label} htmlFor="fl-notes">Anything else about the project? (optional)</label>
          <textarea id="fl-notes" className={s.textarea} maxLength={500}
            placeholder="e.g. 1,800 sq ft on 5 acres, doing my own framing, well and septic"
            value={form.notes} onChange={(e) => set('notes')(e.target.value)} />
        </div>

        {status === 'error' && (
          <p className={s.error} role="alert">
            That didn&apos;t go through. Try again in a minute, or just email
            seth@build-your-house.com with these details.
          </p>
        )}

        <button type="submit" className={s.submit} disabled={status === 'loading'}>
          {status === 'loading' ? 'Sending…' : 'Send my project details'}
        </button>
        <p className={s.fine}>
          Your details go to Seth at Build Your House, and — only if you say yes to an
          introduction — to a lender that writes owner-builder loans in your state.
          You&apos;ll also get the owner-builder newsletter; unsubscribe any time. Never
          sold, never blasted.
        </p>
      </form>
    </div>
  );
}
