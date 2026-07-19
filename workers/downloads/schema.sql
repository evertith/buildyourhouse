-- Download log: one row per successful /download fetch. This is the
-- delivery evidence used when fighting "product not received" disputes.
CREATE TABLE IF NOT EXISTS downloads (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  session_id TEXT NOT NULL,
  email TEXT,
  ip TEXT,
  user_agent TEXT,
  created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_downloads_session ON downloads(session_id);

-- Fulfillment emails sent via Resend on checkout.session.completed.
-- UNIQUE(session_id) is the dedupe guard against Stripe webhook retries.
CREATE TABLE IF NOT EXISTS fulfillment_emails (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  session_id TEXT NOT NULL UNIQUE,
  email TEXT NOT NULL,
  resend_id TEXT,
  created_at TEXT NOT NULL
);

-- Self-service link-recovery attempts (rate-limited per IP).
CREATE TABLE IF NOT EXISTS recovery_requests (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT NOT NULL,
  ip TEXT,
  found INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_recovery_ip ON recovery_requests(ip, created_at);
