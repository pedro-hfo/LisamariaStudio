# ADR-001 · Ferramentas de aprendizagem e desenvolvimento

**Estado:** adotado para a base inicial. **Data:** 2026-11-05.

## Contexto

O criador quer aprender front-end, usar Python com DDD e arquitetura hexagonal, aplicar BDD e manter documentação PT/EN. O projeto começa localmente, para um estúdio com uma profissional.

## Decisão

| Área | Ferramenta | Razão |
|---|---|---|
| Interface | React + TypeScript | Aprender componentes, composição, estado e contratos explícitos |
| Servidor local / build | Vite | Feedback rápido durante a aprendizagem |
| Backend | FastAPI + Python 3.13 | Adapter HTTP pequeno, validação e OpenAPI |
| Dependências Python | uv | Versão de Python isolada e lock reproduzível |
| BDD | pytest-bdd + Gherkin | Exemplos de negócio executáveis em PT/EN |
| Testes front-end | Vitest + React Testing Library | Comportamentos visíveis e integração com Vite |
| Documentação Python e portal | Sphinx + autodoc + MyST + Furo | Referência derivada do código e guias legíveis |
| Documentação TypeScript | TypeDoc + Markdown | Referência do front-end dentro do portal Sphinx |
| Qualidade Python | Ruff + mypy | Consistência e tipos verificados |

## Compatibilidade das dependências

pytest está limitado à versão 8 porque pytest-bdd 8 utiliza uma API interna alterada em pytest 9.2. Os lockfiles registam a combinação verificada.

O TypeDoc atual depende de minimatch 10, afetado por um [aviso moderado sobre processamento de glob patterns](https://github.com/advisories/GHSA-g3hv-75wg-m249). É uma dependência de geração de documentação, usada com caminhos locais do repositório. A substituição por minimatch 11 é incompatível com a API usada pelo TypeDoc; a atualização deve acompanhar uma versão compatível do gerador.

## Consequências práticas

Há dois ecossistemas, npm e Python, coordenados por um comando. Vite serve a aplicação e encaminha `/api` para FastAPI. Não escolhemos uma base de dados nem alojamento nesta etapa. O exemplo em memória permite estudar as fronteiras antes de implementar persistência. Uma SPA Vite não resolve por si só SEO ou renderização no servidor; essa decisão será retomada quando definirmos as páginas públicas.

A demonstração ainda não implementa SIBS nem sincronização em tempo real entre clientes. O catálogo real, preços, cancelamentos e política de preparação continuam por definir.

## Fontes

- [React: começar do zero](https://react.dev/learn/build-a-react-app-from-scratch)
- [Vite](https://vite.dev/guide/)
- [FastAPI: organizar aplicações](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [pytest-bdd](https://pytest-bdd.readthedocs.io/en/stable/)
- [Vitest](https://vitest.dev/guide/)
- [Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
- [Sphinx autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
- [TypeDoc](https://typedoc.org/)
- [uv: locks e sincronização](https://docs.astral.sh/uv/concepts/projects/sync/)
