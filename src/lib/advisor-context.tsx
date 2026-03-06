'use client';

import { createContext, useContext, useState, useEffect, useCallback, ReactNode } from 'react';
import * as api from './advisor-api';

interface AdvisorContextType {
  user: api.User | null;
  loading: boolean;
  login: (email: string, password: string) => Promise<void>;
  signup: (email: string, password: string, name?: string) => Promise<void>;
  logout: () => void;
  refreshUser: () => Promise<void>;
}

const AdvisorContext = createContext<AdvisorContextType | null>(null);

export function AdvisorProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<api.User | null>(null);
  const [loading, setLoading] = useState(true);

  const refreshUser = useCallback(async () => {
    if (!api.isLoggedIn()) {
      setUser(null);
      setLoading(false);
      return;
    }
    try {
      const { user } = await api.getAccount();
      setUser(user);
    } catch {
      // Token invalid or expired
      api.logout();
      setUser(null);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    refreshUser();
  }, [refreshUser]);

  const handleLogin = async (email: string, password: string) => {
    const { user } = await api.login(email, password);
    setUser(user);
  };

  const handleSignup = async (email: string, password: string, name?: string) => {
    const { user } = await api.signup(email, password, name);
    setUser(user);
  };

  const handleLogout = () => {
    api.logout();
    setUser(null);
  };

  return (
    <AdvisorContext.Provider value={{
      user,
      loading,
      login: handleLogin,
      signup: handleSignup,
      logout: handleLogout,
      refreshUser,
    }}>
      {children}
    </AdvisorContext.Provider>
  );
}

export function useAdvisor(): AdvisorContextType {
  const context = useContext(AdvisorContext);
  if (!context) {
    throw new Error('useAdvisor must be used within an AdvisorProvider');
  }
  return context;
}
