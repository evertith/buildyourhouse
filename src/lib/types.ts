export interface ArticleMetadata {
  title: string;
  description: string;
  author: string;
  date: string;
  updated?: string;
  category: string;
  tags: string[];
  difficulty?: 'beginner' | 'intermediate' | 'advanced';
  readTime?: string;
  featured?: boolean;
  slug: string;
}

export interface NavigationLink {
  href: string;
  label: string;
  children?: NavigationLink[];
}

export interface BuildPhase {
  id: string;
  title: string;
  order: number;
  duration: string;
  difficulty: number;
  diyRecommended: boolean;
  slug: string;
}
