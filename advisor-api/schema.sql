-- Users table
CREATE TABLE IF NOT EXISTS users (
  id TEXT PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  name TEXT,
  stripe_customer_id TEXT,
  subscription_status TEXT DEFAULT 'none',
  subscription_id TEXT,
  plan TEXT DEFAULT 'free',
  queries_used_this_month INTEGER DEFAULT 0,
  queries_reset_at TEXT,
  created_at TEXT DEFAULT (datetime('now')),
  updated_at TEXT DEFAULT (datetime('now'))
);

-- Build profiles
CREATE TABLE IF NOT EXISTS builds (
  id TEXT PRIMARY KEY,
  user_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  name TEXT DEFAULT 'My Build',
  state TEXT NOT NULL,
  county TEXT,
  phase TEXT NOT NULL DEFAULT 'researching',
  square_footage INTEGER,
  stories INTEGER DEFAULT 1,
  foundation_type TEXT,
  build_approach TEXT DEFAULT 'mix',
  budget_range TEXT,
  timeline_goal TEXT,
  has_land INTEGER DEFAULT 0,
  has_plans INTEGER DEFAULT 0,
  has_permit INTEGER DEFAULT 0,
  has_loan INTEGER DEFAULT 0,
  notes TEXT,
  created_at TEXT DEFAULT (datetime('now')),
  updated_at TEXT DEFAULT (datetime('now'))
);

-- Build memories (extracted facts)
CREATE TABLE IF NOT EXISTS memories (
  id TEXT PRIMARY KEY,
  build_id TEXT NOT NULL REFERENCES builds(id) ON DELETE CASCADE,
  fact TEXT NOT NULL,
  category TEXT NOT NULL,
  source_conversation_id TEXT,
  created_at TEXT DEFAULT (datetime('now'))
);

-- Conversations
CREATE TABLE IF NOT EXISTS conversations (
  id TEXT PRIMARY KEY,
  build_id TEXT NOT NULL REFERENCES builds(id) ON DELETE CASCADE,
  title TEXT,
  summary TEXT,
  messages TEXT NOT NULL DEFAULT '[]',
  created_at TEXT DEFAULT (datetime('now')),
  updated_at TEXT DEFAULT (datetime('now'))
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_builds_user_id ON builds(user_id);
CREATE INDEX IF NOT EXISTS idx_memories_build_id ON memories(build_id);
CREATE INDEX IF NOT EXISTS idx_conversations_build_id ON conversations(build_id);
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_users_stripe_customer_id ON users(stripe_customer_id);
