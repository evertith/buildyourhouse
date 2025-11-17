import createMDX from '@next/mdx';

/** @type {import('next').NextConfig} */
const nextConfig = {
  pageExtensions: ['js', 'jsx', 'md', 'mdx', 'ts', 'tsx'],
  output: 'export',
  images: {
    unoptimized: true
  },
  // Increase static generation timeout for Cloudflare Pages
  staticPageGenerationTimeout: 180,
  // Reduce parallelization to avoid memory issues on Cloudflare
  experimental: {
    workerThreads: false,
    cpus: 1
  }
};

const withMDX = createMDX();

export default withMDX(nextConfig);
