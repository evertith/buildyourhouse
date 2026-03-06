import { AdvisorProvider } from '@/lib/advisor-context';

export default function AdvisorLayout({ children }: { children: React.ReactNode }) {
  return <AdvisorProvider>{children}</AdvisorProvider>;
}
