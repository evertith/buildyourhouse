'use client';

import { useState, useRef, useEffect } from 'react';
import styles from '@/styles/ChatInterface.module.css';

interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: number;
}

interface ChatInterfaceProps {
  apiEndpoint?: string;
}

export default function ChatInterface({ apiEndpoint }: ChatInterfaceProps) {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: 'welcome',
      role: 'assistant',
      content:
        "Hey, I'm Reed — a retired general contractor turned AI advisor. I've built custom homes for 15+ years, and now I'm here to help you build yours. What's on your mind?",
      timestamp: Date.now(),
    },
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || isLoading) return;

    const userMessage: Message = {
      id: `user-${Date.now()}`,
      role: 'user',
      content: input.trim(),
      timestamp: Date.now(),
    };

    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      if (!apiEndpoint) {
        // Demo mode — no backend connected yet
        await new Promise(resolve => setTimeout(resolve, 1500));
        const demoResponse: Message = {
          id: `assistant-${Date.now()}`,
          role: 'assistant',
          content:
            "Reed is being set up! The AI general contractor backend isn't connected yet. Once Builder Pro launches, I'll be able to answer your construction questions with code-specific, jurisdiction-aware advice. Stay tuned!",
          timestamp: Date.now(),
        };
        setMessages(prev => [...prev, demoResponse]);
        return;
      }

      const res = await fetch(apiEndpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          messages: [...messages, userMessage].map(m => ({
            role: m.role,
            content: m.content,
          })),
        }),
      });

      if (!res.ok) throw new Error('Failed to get response');

      const data = await res.json();
      const assistantMessage: Message = {
        id: `assistant-${Date.now()}`,
        role: 'assistant',
        content: data.message || data.content || 'Sorry, I had trouble processing that. Try again?',
        timestamp: Date.now(),
      };
      setMessages(prev => [...prev, assistantMessage]);
    } catch {
      setMessages(prev => [
        ...prev,
        {
          id: `error-${Date.now()}`,
          role: 'assistant',
          content: "Something went wrong. Let me try again — or you can rephrase your question.",
          timestamp: Date.now(),
        },
      ]);
    } finally {
      setIsLoading(false);
      inputRef.current?.focus();
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  return (
    <div className={styles.chatContainer}>
      <div className={styles.chatHeader}>
        <div className={styles.headerAvatar}>R</div>
        <div>
          <div className={styles.headerName}>Reed</div>
          <div className={styles.headerSubtitle}>AI General Contractor</div>
        </div>
      </div>

      <div className={styles.messagesContainer}>
        {messages.map(msg => (
          <div
            key={msg.id}
            className={`${styles.message} ${
              msg.role === 'user' ? styles.userMessage : styles.assistantMessage
            }`}
          >
            {msg.role === 'assistant' && (
              <div className={styles.msgAvatar}>R</div>
            )}
            <div className={styles.msgBubble}>
              {msg.content.split('\n').map((line, i) => (
                <p key={i}>{line || '\u00A0'}</p>
              ))}
            </div>
          </div>
        ))}

        {isLoading && (
          <div className={`${styles.message} ${styles.assistantMessage}`}>
            <div className={styles.msgAvatar}>R</div>
            <div className={styles.msgBubble}>
              <div className={styles.typingIndicator}>
                <span></span><span></span><span></span>
              </div>
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      <form onSubmit={handleSubmit} className={styles.inputForm}>
        <textarea
          ref={inputRef}
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Ask Reed about your build..."
          className={styles.inputField}
          rows={1}
          disabled={isLoading}
        />
        <button
          type="submit"
          className={styles.sendButton}
          disabled={isLoading || !input.trim()}
        >
          Send
        </button>
      </form>
    </div>
  );
}
