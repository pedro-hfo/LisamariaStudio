import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';

export default defineConfig({
  base: process.env.PAGES_BASE_PATH || '/',
  plugins: [react()],
  server: {
    host: '127.0.0.1',
    strictPort: true,
    proxy: { '/api': process.env.LISAMARIA_API_URL ?? 'http://127.0.0.1:8000' },
  },
  test: {
    environment: 'jsdom', setupFiles: ['./tests/setup.ts'],
    include: ['tests/**/*.test.{ts,tsx}', '../acceptance/frontend/**/*.test.{ts,tsx}'],
  },
});
