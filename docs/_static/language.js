document.addEventListener('DOMContentLoaded', () => {
  const current = location.pathname.includes('/en/') ? 'en' : 'pt';
  document.documentElement.lang = current === 'pt' ? 'pt-PT' : 'en';
  const bar = document.createElement('nav');
  bar.className = 'language-switch';
  bar.setAttribute('aria-label', 'Language / Idioma');
  const link = document.createElement('a');
  link.textContent = current === 'pt' ? 'Read this page in English →' : 'Ler esta página em português →';
  link.href = location.pathname.includes(`/${current}/`)
    ? location.pathname.replace(`/${current}/`, current === 'pt' ? '/en/' : '/pt/')
    : current === 'pt' ? 'en/index.html' : 'pt/index.html';
  bar.append(link);
  document.querySelector('.main')?.prepend(bar);
});
