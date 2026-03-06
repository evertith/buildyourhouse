const API_BASE = process.env.NEXT_PUBLIC_ADVISOR_API_URL || 'https://buildyourhouse-advisor-api.azerothcorner.workers.dev';

class AdvisorApiError extends Error {
  status: number;
  data: Record<string, unknown>;
  constructor(message: string, status: number, data: Record<string, unknown> = {}) {
    super(message);
    this.status = status;
    this.data = data;
  }
}

function getToken(): string | null {
  if (typeof window === 'undefined') return null;
  return localStorage.getItem('advisor_token');
}

async function request<T>(path: string, options: RequestInit = {}): Promise<T> {
  const token = getToken();
  const headers: Record<string, string> = {
    'Content-Type': 'application/json',
    ...(options.headers as Record<string, string> || {}),
  };
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }

  const res = await fetch(`${API_BASE}${path}`, {
    ...options,
    headers,
    credentials: 'include',
  });

  if (!res.ok) {
    const data = await res.json().catch(() => ({})) as Record<string, unknown>;
    throw new AdvisorApiError(
      (data.error as string) || `Request failed with status ${res.status}`,
      res.status,
      data
    );
  }

  return res.json() as Promise<T>;
}

// Auth
export interface User {
  id: string;
  email: string;
  name: string | null;
  plan: string;
  subscription_status: string;
}

export interface AuthResponse {
  token: string;
  user: User;
}

export async function signup(email: string, password: string, name?: string): Promise<AuthResponse> {
  const data = await request<AuthResponse>('/auth/signup', {
    method: 'POST',
    body: JSON.stringify({ email, password, name }),
  });
  localStorage.setItem('advisor_token', data.token);
  return data;
}

export async function login(email: string, password: string): Promise<AuthResponse> {
  const data = await request<AuthResponse>('/auth/login', {
    method: 'POST',
    body: JSON.stringify({ email, password }),
  });
  localStorage.setItem('advisor_token', data.token);
  return data;
}

export function logout(): void {
  localStorage.removeItem('advisor_token');
}

export function isLoggedIn(): boolean {
  return !!getToken();
}

// Builds
export interface Build {
  id: string;
  user_id: string;
  name: string;
  state: string;
  county: string | null;
  phase: string;
  square_footage: number | null;
  stories: number | null;
  foundation_type: string | null;
  build_approach: string;
  budget_range: string | null;
  timeline_goal: string | null;
  has_land: number;
  has_plans: number;
  has_permit: number;
  has_loan: number;
  notes: string | null;
  created_at: string;
  updated_at: string;
}

export async function listBuilds(): Promise<Build[]> {
  const data = await request<{ builds: Build[] }>('/builds');
  return data.builds;
}

export async function createBuild(build: Partial<Build>): Promise<Build> {
  const data = await request<{ build: Build }>('/builds', {
    method: 'POST',
    body: JSON.stringify(build),
  });
  return data.build;
}

export async function getBuild(id: string): Promise<Build> {
  const data = await request<{ build: Build }>(`/builds/${id}`);
  return data.build;
}

export async function updateBuild(id: string, updates: Partial<Build>): Promise<Build> {
  const data = await request<{ build: Build }>(`/builds/${id}`, {
    method: 'PUT',
    body: JSON.stringify(updates),
  });
  return data.build;
}

export async function deleteBuild(id: string): Promise<void> {
  await request(`/builds/${id}`, { method: 'DELETE' });
}

// Conversations
export interface Conversation {
  id: string;
  build_id: string;
  title: string | null;
  summary: string | null;
  messages: string; // JSON string of Message[]
  created_at: string;
  updated_at: string;
}

export interface Message {
  role: 'user' | 'assistant';
  content: string;
}

export async function listConversations(buildId: string): Promise<Conversation[]> {
  const data = await request<{ conversations: Conversation[] }>(`/conversations?build_id=${buildId}`);
  return data.conversations;
}

export async function getConversation(id: string): Promise<Conversation> {
  const data = await request<{ conversation: Conversation }>(`/conversations/${id}`);
  return data.conversation;
}

export async function deleteConversation(id: string): Promise<void> {
  await request(`/conversations/${id}`, { method: 'DELETE' });
}

// Chat (streaming)
export interface ChatStreamEvent {
  text?: string;
  done?: boolean;
  conversation_id?: string;
  error?: string;
}

export async function* streamChat(
  buildId: string,
  message: string,
  conversationId?: string
): AsyncGenerator<ChatStreamEvent> {
  const token = getToken();
  const res = await fetch(`${API_BASE}/chat`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`,
    },
    body: JSON.stringify({
      build_id: buildId,
      message,
      conversation_id: conversationId,
    }),
  });

  if (!res.ok) {
    const data = await res.json().catch(() => ({})) as Record<string, unknown>;
    throw new AdvisorApiError(
      (data.error as string) || 'Chat request failed',
      res.status,
      data
    );
  }

  const reader = res.body!.getReader();
  const decoder = new TextDecoder();
  let buffer = '';

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    buffer += decoder.decode(value, { stream: true });
    const lines = buffer.split('\n');
    buffer = lines.pop() || '';

    for (const line of lines) {
      if (line.startsWith('data: ')) {
        try {
          const event = JSON.parse(line.slice(6)) as ChatStreamEvent;
          yield event;
        } catch {
          // Skip malformed events
        }
      }
    }
  }
}

// Account
export interface Usage {
  plan: string;
  subscription_status: string;
  queries_used: number;
  queries_limit: number;
  resets_at: string;
}

export async function getAccount(): Promise<{ user: User }> {
  return request<{ user: User }>('/account');
}

export async function getUsage(): Promise<Usage> {
  return request<Usage>('/account/usage');
}

export async function createCheckoutSession(plan: string): Promise<{ url: string }> {
  return request<{ url: string }>('/account/subscribe', {
    method: 'POST',
    body: JSON.stringify({ plan }),
  });
}

export async function createPortalSession(): Promise<{ url: string }> {
  return request<{ url: string }>('/account/portal', { method: 'POST' });
}

export { AdvisorApiError };
