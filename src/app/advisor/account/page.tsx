'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import { useAdvisor } from '@/lib/advisor-context';
import * as api from '@/lib/advisor-api';
import styles from '@/styles/AdvisorAccount.module.css';

export default function AccountPage() {
  const router = useRouter();
  const { user, loading: authLoading, logout } = useAdvisor();
  const [usage, setUsage] = useState<api.Usage | null>(null);
  const [builds, setBuilds] = useState<api.Build[]>([]);
  const [loadingAction, setLoadingAction] = useState('');

  useEffect(() => {
    if (authLoading) return;
    if (!user) {
      router.push('/advisor/login');
      return;
    }

    async function loadData() {
      try {
        const [usageData, buildsData] = await Promise.all([
          api.getUsage(),
          api.listBuilds(),
        ]);
        setUsage(usageData);
        setBuilds(buildsData);
      } catch {
        router.push('/advisor/login');
      }
    }

    loadData();
  }, [authLoading, user, router]);

  const handleSubscribe = async (plan: string) => {
    setLoadingAction(plan);
    try {
      const { url } = await api.createCheckoutSession(plan);
      window.location.href = url;
    } catch {
      alert('Failed to create checkout session. Please try again.');
    } finally {
      setLoadingAction('');
    }
  };

  const handleManageSubscription = async () => {
    setLoadingAction('portal');
    try {
      const { url } = await api.createPortalSession();
      window.location.href = url;
    } catch {
      alert('Failed to open billing portal. Please try again.');
    } finally {
      setLoadingAction('');
    }
  };

  const handleLogout = () => {
    logout();
    router.push('/advisor/login');
  };

  if (authLoading || !user) return null;

  const usagePercent = usage ? Math.min((usage.queries_used / usage.queries_limit) * 100, 100) : 0;
  const usageFillClass = usagePercent > 90 ? styles.usageFillCritical : usagePercent > 70 ? styles.usageFillWarning : '';

  return (
    <div className={styles.container}>
      <Link href="/advisor/chat" className={styles.backLink}>
        &#8592; Back to Chat
      </Link>

      <h1 className={styles.title}>Account</h1>

      {/* Profile Section */}
      <div className={styles.section}>
        <h2 className={styles.sectionTitle}>Profile</h2>
        <div className={styles.row}>
          <span className={styles.rowLabel}>Email</span>
          <span className={styles.rowValue}>{user.email}</span>
        </div>
        {user.name && (
          <div className={styles.row}>
            <span className={styles.rowLabel}>Name</span>
            <span className={styles.rowValue}>{user.name}</span>
          </div>
        )}
        <div className={styles.row}>
          <span className={styles.rowLabel}>Plan</span>
          <span className={`${styles.badge} ${user.plan === 'free' ? styles.badgeFree : styles.badgeActive}`}>
            {user.plan}
          </span>
        </div>
      </div>

      {/* Usage Section */}
      {usage && (
        <div className={styles.section}>
          <h2 className={styles.sectionTitle}>Usage This Month</h2>
          <div className={styles.usageMeter}>
            <div className={styles.usageBar}>
              <div
                className={`${styles.usageFill} ${usageFillClass}`}
                style={{ width: `${usagePercent}%` }}
              />
            </div>
            <div className={styles.usageText}>
              <span>{usage.queries_used} questions used</span>
              <span>{usage.queries_limit} limit</span>
            </div>
          </div>
        </div>
      )}

      {/* Subscription Section */}
      <div className={styles.section}>
        <h2 className={styles.sectionTitle}>
          {user.plan === 'free' ? 'Upgrade Your Plan' : 'Subscription'}
        </h2>

        {user.plan === 'free' ? (
          <>
            <p style={{ color: 'var(--text-secondary)', marginBottom: 'var(--space-2)', fontSize: 'var(--text-sm)' }}>
              Get more questions and unlock the full power of your AI construction advisor.
            </p>
            <div className={styles.planCards}>
              <div className={styles.planCard}>
                <div className={styles.planName}>Starter</div>
                <div className={styles.planPrice}>$19<span>/mo</span></div>
                <div className={styles.planFeature}>50 questions/month</div>
                <div className={styles.planFeature}>Full project memory</div>
                <div className={styles.planFeature}>All state guides</div>
                <button
                  className={styles.actionButton}
                  onClick={() => handleSubscribe('starter')}
                  disabled={!!loadingAction}
                  style={{ width: '100%', marginTop: 'var(--space-2)' }}
                >
                  {loadingAction === 'starter' ? 'Loading...' : 'Get Starter'}
                </button>
              </div>
              <div className={styles.planCard}>
                <div className={styles.planName}>Pro</div>
                <div className={styles.planPrice}>$29<span>/mo</span></div>
                <div className={styles.planFeature}>200 questions/month</div>
                <div className={styles.planFeature}>Full project memory</div>
                <div className={styles.planFeature}>Priority responses</div>
                <button
                  className={styles.actionButton}
                  onClick={() => handleSubscribe('pro')}
                  disabled={!!loadingAction}
                  style={{ width: '100%', marginTop: 'var(--space-2)' }}
                >
                  {loadingAction === 'pro' ? 'Loading...' : 'Get Pro'}
                </button>
              </div>
            </div>
          </>
        ) : (
          <div>
            <div className={styles.row}>
              <span className={styles.rowLabel}>Status</span>
              <span className={`${styles.badge} ${styles.badgeActive}`}>
                {usage?.subscription_status || 'active'}
              </span>
            </div>
            <button
              className={styles.secondaryButton}
              onClick={handleManageSubscription}
              disabled={!!loadingAction}
              style={{ marginTop: 'var(--space-2)' }}
            >
              {loadingAction === 'portal' ? 'Loading...' : 'Manage Subscription'}
            </button>
          </div>
        )}
      </div>

      {/* Builds Section */}
      {builds.length > 0 && (
        <div className={styles.section}>
          <h2 className={styles.sectionTitle}>Your Builds</h2>
          {builds.map(build => (
            <div key={build.id} className={styles.row}>
              <div>
                <span className={styles.rowValue}>{build.name}</span>
                <br />
                <span className={styles.rowLabel}>
                  {build.state.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase())}
                  {build.county ? `, ${build.county}` : ''} — {build.phase.replace(/-/g, ' ')}
                </span>
              </div>
              <button
                className={styles.secondaryButton}
                onClick={() => {
                  localStorage.setItem('advisor_active_build', build.id);
                  router.push('/advisor/chat');
                }}
              >
                Chat
              </button>
            </div>
          ))}
          <button
            className={styles.secondaryButton}
            onClick={() => router.push('/advisor/onboarding')}
            style={{ marginTop: 'var(--space-2)' }}
          >
            + Add Another Build
          </button>
        </div>
      )}

      {/* Danger Zone */}
      <div className={styles.section}>
        <div className={styles.row}>
          <span className={styles.rowLabel}>Sign out of your account</span>
          <button className={styles.dangerButton} onClick={handleLogout}>
            Sign Out
          </button>
        </div>
      </div>
    </div>
  );
}
