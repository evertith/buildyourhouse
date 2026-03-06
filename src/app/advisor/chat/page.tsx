'use client';

import { useState, useEffect, useRef, useCallback } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import { useAdvisor } from '@/lib/advisor-context';
import * as api from '@/lib/advisor-api';
import styles from '@/styles/AdvisorChat.module.css';

interface ChatMessage {
  role: 'user' | 'assistant';
  content: string;
}

const SUGGESTIONS = [
  'What should I do first as an owner-builder?',
  'How do I find reliable subcontractors?',
  'What permits do I need in my state?',
  'How much should I budget for contingencies?',
  'What inspections will I need to pass?',
  'Should I hire an electrician or DIY?',
];

function renderMarkdown(text: string): string {
  return text
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\n\n/g, '</p><p>')
    .replace(/\n- /g, '</p><ul><li>')
    .replace(/\n(\d+)\. /g, '</p><ol><li>')
    .replace(/<\/li>\n- /g, '</li><li>')
    .replace(/<\/li>\n(\d+)\. /g, '</li><li>')
    .replace(/<ul><li>([\s\S]*?)(?=<\/p>|$)/g, (match) => {
      if (!match.endsWith('</ul>')) return match + '</li></ul>';
      return match;
    })
    .replace(/<ol><li>([\s\S]*?)(?=<\/p>|$)/g, (match) => {
      if (!match.endsWith('</ol>')) return match + '</li></ol>';
      return match;
    });
}

export default function ChatPage() {
  const router = useRouter();
  const { user, loading: authLoading } = useAdvisor();
  const [build, setBuild] = useState<api.Build | null>(null);
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState('');
  const [streaming, setStreaming] = useState(false);
  const [conversationId, setConversationId] = useState<string | undefined>();
  const [usage, setUsage] = useState<api.Usage | null>(null);
  const [buildLoading, setBuildLoading] = useState(true);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  const scrollToBottom = useCallback(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, []);

  // Load build and usage on mount
  useEffect(() => {
    if (authLoading) return;
    if (!user) {
      router.push('/advisor/login');
      return;
    }

    async function loadData() {
      try {
        // Try to load active build
        const activeBuildId = localStorage.getItem('advisor_active_build');
        const builds = await api.listBuilds();

        if (builds.length === 0) {
          router.push('/advisor/onboarding');
          return;
        }

        const activeBuild = activeBuildId
          ? builds.find(b => b.id === activeBuildId) || builds[0]
          : builds[0];

        setBuild(activeBuild);
        localStorage.setItem('advisor_active_build', activeBuild.id);

        // Load usage
        const usageData = await api.getUsage();
        setUsage(usageData);
      } catch {
        // If token is invalid, redirect to login
        router.push('/advisor/login');
      } finally {
        setBuildLoading(false);
      }
    }

    loadData();
  }, [authLoading, user, router]);

  // Auto-scroll on new messages
  useEffect(() => {
    scrollToBottom();
  }, [messages, scrollToBottom]);

  // Auto-resize textarea
  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
      textareaRef.current.style.height = Math.min(textareaRef.current.scrollHeight, 150) + 'px';
    }
  }, [input]);

  const sendMessage = async (text?: string) => {
    const messageText = text || input.trim();
    if (!messageText || streaming || !build) return;

    setInput('');
    setMessages(prev => [...prev, { role: 'user', content: messageText }]);
    setStreaming(true);

    // Add empty assistant message that we'll stream into
    setMessages(prev => [...prev, { role: 'assistant', content: '' }]);

    try {
      for await (const event of api.streamChat(build.id, messageText, conversationId)) {
        if (event.text) {
          setMessages(prev => {
            const updated = [...prev];
            const last = updated[updated.length - 1];
            if (last.role === 'assistant') {
              last.content += event.text;
            }
            return [...updated];
          });
        }
        if (event.conversation_id) {
          setConversationId(event.conversation_id);
        }
        if (event.error) {
          setMessages(prev => {
            const updated = [...prev];
            const last = updated[updated.length - 1];
            if (last.role === 'assistant') {
              last.content = 'Sorry, something went wrong. Please try again.';
            }
            return [...updated];
          });
        }
      }

      // Refresh usage
      const usageData = await api.getUsage();
      setUsage(usageData);
    } catch (err) {
      if (err instanceof api.AdvisorApiError && err.data.limit_reached) {
        setMessages(prev => {
          const updated = [...prev];
          const last = updated[updated.length - 1];
          if (last.role === 'assistant') {
            last.content = `You've reached your monthly query limit (${usage?.queries_limit || 5} questions). Upgrade your plan to continue chatting.`;
          }
          return [...updated];
        });
      } else {
        setMessages(prev => {
          const updated = [...prev];
          const last = updated[updated.length - 1];
          if (last.role === 'assistant') {
            last.content = 'Sorry, something went wrong. Please try again.';
          }
          return [...updated];
        });
      }
    } finally {
      setStreaming(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const startNewConversation = () => {
    setMessages([]);
    setConversationId(undefined);
  };

  if (authLoading || buildLoading) {
    return (
      <div className={styles.container}>
        <div className={styles.welcome}>
          <p>Loading...</p>
        </div>
      </div>
    );
  }

  if (!build) return null;

  const phaseDisplay = build.phase.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase());

  return (
    <div className={styles.container}>
      {/* Header */}
      <div className={styles.header}>
        <div className={styles.headerLeft}>
          <span className={styles.buildName}>{build.name}</span>
          <span className={styles.buildPhase}>{phaseDisplay}</span>
        </div>
        <div className={styles.headerActions}>
          <button className={styles.headerButton} onClick={startNewConversation}>
            + New Chat
          </button>
          <Link href="/advisor/account" className={styles.headerButton}>
            Account
          </Link>
        </div>
      </div>

      {/* Messages */}
      <div className={styles.messages}>
        {messages.length === 0 ? (
          <div className={styles.welcome}>
            <h2 className={styles.welcomeTitle}>Your Build Advisor</h2>
            <p className={styles.welcomeSubtitle}>
              Ask me anything about your build in {build.state.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase())}.
              I&apos;ll give you specific, actionable advice.
            </p>
            <div className={styles.suggestions}>
              {SUGGESTIONS.map((s, i) => (
                <button
                  key={i}
                  className={styles.suggestion}
                  onClick={() => sendMessage(s)}
                >
                  {s}
                </button>
              ))}
            </div>
          </div>
        ) : (
          <>
            {messages.map((msg, i) => (
              <div
                key={i}
                className={msg.role === 'user' ? styles.messageUser : styles.messageAssistant}
              >
                {msg.role === 'assistant' ? (
                  <div dangerouslySetInnerHTML={{ __html: `<p>${renderMarkdown(msg.content)}</p>` }} />
                ) : (
                  msg.content
                )}
              </div>
            ))}
            {streaming && messages[messages.length - 1]?.content === '' && (
              <div className={styles.typing}>
                <div className={styles.typingDot} />
                <div className={styles.typingDot} />
                <div className={styles.typingDot} />
              </div>
            )}
          </>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <div className={styles.inputArea}>
        <div className={styles.inputRow}>
          <textarea
            ref={textareaRef}
            className={styles.textInput}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Ask about your build..."
            rows={1}
            disabled={streaming}
          />
          <button
            className={styles.sendButton}
            onClick={() => sendMessage()}
            disabled={streaming || !input.trim()}
            aria-label="Send message"
          >
            &#8593;
          </button>
        </div>
        {usage && (
          <div className={styles.usageBar}>
            <span>{usage.queries_used} / {usage.queries_limit} questions this month</span>
            {usage.plan === 'free' && (
              <Link href="/advisor/account">Upgrade for more</Link>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
