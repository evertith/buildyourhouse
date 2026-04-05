'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';
import styles from '@/styles/ChatPreview.module.css';

const DEMO_MESSAGES = [
  {
    role: 'user' as const,
    text: "I'm building a 2,400 sq ft house in Wake County, NC. What permits do I need?",
  },
  {
    role: 'assistant' as const,
    text: `Great question! For a 2,400 sq ft new construction in Wake County, NC, you'll need:

**Required permits:**
- Building permit (residential new construction)
- Electrical permit
- Plumbing permit
- Mechanical/HVAC permit
- Well permit (if not on municipal water)
- Septic permit (if not on municipal sewer)

**Wake County specifics:**
- NC doesn't require a general contractor's license for owner-builders on their own primary residence
- You'll need to file an owner-builder affidavit
- Plan review typically takes 2-3 weeks
- Expect \$3,500-\$5,500 in total permit fees for that size

Want me to walk you through the application process step by step?`,
  },
  {
    role: 'user' as const,
    text: "Yes! And how long should I expect the whole build to take?",
  },
  {
    role: 'assistant' as const,
    text: `For a 2,400 sq ft owner-builder project in the Raleigh area, here's a realistic timeline:

**Total: 10-14 months** (assuming you're managing full-time)

- Site work & foundation: 3-5 weeks
- Framing: 3-4 weeks
- Roofing & exterior: 2-3 weeks
- Rough-ins (electrical, plumbing, HVAC): 3-4 weeks
- Insulation & drywall: 3-4 weeks
- Interior finishes: 6-8 weeks
- Final inspections & punch list: 2-3 weeks

**Pro tip:** Wake County inspectors are generally responsive — most inspections scheduled within 48 hours. Don't let inspection scheduling become your bottleneck. Have your next phase ready to go before the current inspection.`,
  },
];

export default function ChatPreview() {
  const [visibleMessages, setVisibleMessages] = useState(0);

  useEffect(() => {
    if (visibleMessages < DEMO_MESSAGES.length) {
      const delay = visibleMessages === 0 ? 500 : visibleMessages % 2 === 0 ? 1500 : 2000;
      const timer = setTimeout(() => {
        setVisibleMessages(prev => prev + 1);
      }, delay);
      return () => clearTimeout(timer);
    }
  }, [visibleMessages]);

  return (
    <div className={styles.chatPreview}>
      <div className={styles.chatHeader}>
        <div className={styles.chatAvatar}>R</div>
        <div>
          <div className={styles.chatName}>Reed</div>
          <div className={styles.chatStatus}>AI General Contractor</div>
        </div>
      </div>

      <div className={styles.chatMessages}>
        {DEMO_MESSAGES.slice(0, visibleMessages).map((msg, i) => (
          <div
            key={i}
            className={`${styles.message} ${
              msg.role === 'user' ? styles.messageUser : styles.messageAssistant
            }`}
          >
            {msg.role === 'assistant' && (
              <div className={styles.messageAvatar}>R</div>
            )}
            <div className={styles.messageBubble}>
              {msg.text.split('\n').map((line, j) => {
                if (line.startsWith('**') && line.endsWith('**')) {
                  return <p key={j}><strong>{line.replace(/\*\*/g, '')}</strong></p>;
                }
                if (line.startsWith('- ')) {
                  return <p key={j} className={styles.listItem}>{line}</p>;
                }
                if (line === '') return <br key={j} />;
                return <p key={j}>{line}</p>;
              })}
            </div>
          </div>
        ))}

        {visibleMessages < DEMO_MESSAGES.length && visibleMessages > 0 && visibleMessages % 2 !== 0 && (
          <div className={`${styles.message} ${styles.messageAssistant}`}>
            <div className={styles.messageAvatar}>R</div>
            <div className={styles.messageBubble}>
              <div className={styles.typing}>
                <span></span><span></span><span></span>
              </div>
            </div>
          </div>
        )}
      </div>

      <div className={styles.chatFooter}>
        <Link href="/pricing" className={styles.tryButton}>
          Try Reed with Builder Pro — $20/month
        </Link>
      </div>
    </div>
  );
}
