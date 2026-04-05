import type { Metadata } from 'next';
import ChatInterface from '@/components/ChatInterface';

export const metadata: Metadata = {
  title: 'Chat with Reed — AI General Contractor',
  description:
    'Ask Reed, your AI general contractor, anything about your owner-builder project. Get code-specific answers, material estimates, and inspection prep — 24/7.',
  robots: { index: false, follow: false },
};

const REED_API_URL = process.env.NEXT_PUBLIC_REED_API_URL || '';

export default function ChatPage() {
  return (
    <div style={{ padding: '0', maxWidth: '100%' }}>
      <ChatInterface apiEndpoint={REED_API_URL || undefined} />
    </div>
  );
}
