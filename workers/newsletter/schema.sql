CREATE TABLE IF NOT EXISTS subscribers (
  email TEXT PRIMARY KEY,
  source TEXT,
  created_at TEXT NOT NULL,
  unsubscribed_at TEXT
);
