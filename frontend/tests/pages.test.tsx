import { render, screen } from '@testing-library/react';
import { afterEach, expect, it, vi } from 'vitest';
import { App } from '../src/App';

afterEach(() => {
  vi.unstubAllEnvs();
  vi.unstubAllGlobals();
});

it('Pages presents guides under the repository path without contacting a backend / Pages sem API', () => {
  vi.stubEnv('MODE', 'pages');
  vi.stubEnv('BASE_URL', '/LisamariaStudio/');
  const fetch = vi.fn();
  vi.stubGlobal('fetch', fetch);
  render(<App />);
  expect(screen.queryByRole('button')).not.toBeInTheDocument();
  expect(fetch).not.toHaveBeenCalled();
  expect(screen.getByRole('link', { name: /Experimentar localmente/ })).toHaveAttribute(
    'href', '/LisamariaStudio/docs/pt/getting-started.html');
  expect(screen.getByRole('link', { name: /English guide/ })).toHaveAttribute(
    'href', '/LisamariaStudio/docs/en/index.html');
  for (const link of screen.getAllByRole('link')) {
    expect(link.getAttribute('href')).toMatch(/^\/LisamariaStudio\//);
  }
});
