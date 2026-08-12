CREATE TABLE IF NOT EXISTS subscribers (
  email TEXT PRIMARY KEY,
  source TEXT,
  created_at TEXT NOT NULL,
  unsubscribed_at TEXT
);

-- Owner-builder financing leads (the qualified-lead product from
-- lender-outreach/pricing-sheet.md §2). status tracks the handoff pipeline:
-- 'new' → 'sent' (forwarded to a lender, sent_to = lender id) → 'rejected'
-- (lender bounced it inside the agreed 48-72h window).
CREATE TABLE IF NOT EXISTS financing_leads (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created_at TEXT NOT NULL,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  phone TEXT NOT NULL,
  state TEXT NOT NULL,
  timeline TEXT NOT NULL,
  credit_band TEXT NOT NULL,
  land_status TEXT NOT NULL,
  budget_band TEXT,
  notes TEXT,
  source TEXT,
  status TEXT NOT NULL DEFAULT 'new',
  sent_to TEXT
);
