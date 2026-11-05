# ADR-001 · Learning and development tools

**Status:** adopted for the initial foundation. **Date:** 2026-11-05.

## Context

The creator wants to learn frontend development, use Python with DDD and hexagonal architecture, apply BDD and maintain PT/EN documentation. The project starts locally for a studio with one practitioner.

## Decision

| Area | Tool | Reason |
|---|---|---|
| Interface | React + TypeScript | Learn components, composition, state and explicit contracts |
| Local server / build | Vite | Fast feedback while learning |
| Backend | FastAPI + Python 3.13 | Small HTTP adapter, validation and OpenAPI |
| Python dependencies | uv | Isolated Python version and reproducible lock |
| BDD | pytest-bdd + Gherkin | Executable PT/EN business examples |
| Frontend tests | Vitest + React Testing Library | Visible behaviours and Vite integration |
| Python documentation and portal | Sphinx + autodoc + MyST + Furo | Code-derived references and readable guides |
| TypeScript documentation | TypeDoc + Markdown | Frontend reference inside the Sphinx portal |
| Python quality | Ruff + mypy | Consistency and checked types |

## Dependency compatibility

pytest is limited to version 8 because pytest-bdd 8 uses an internal API changed in pytest 9.2. The lockfiles record the verified combination.

Current TypeDoc depends on minimatch 10, affected by a [moderate glob-pattern processing advisory](https://github.com/advisories/GHSA-g3hv-75wg-m249). This is a documentation-generation dependency used with local repository paths. Substituting minimatch 11 is incompatible with the API used by TypeDoc; upgrade alongside a compatible generator version.

## Practical consequences

There are two ecosystems, npm and Python, coordinated by one command. Vite serves the application and proxies `/api` to FastAPI. We have not selected a database or hosting platform at this stage. The in-memory example lets us study boundaries before implementing persistence. A Vite SPA does not itself solve SEO or server rendering; we will revisit that decision when defining public pages.

The demonstration does not yet implement SIBS or real-time synchronisation across clients. The actual service catalogue, prices, cancellations and preparation policy remain to be defined.

## Sources

- [React: building from scratch](https://react.dev/learn/build-a-react-app-from-scratch)
- [Vite](https://vite.dev/guide/)
- [FastAPI: organising applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [pytest-bdd](https://pytest-bdd.readthedocs.io/en/stable/)
- [Vitest](https://vitest.dev/guide/)
- [Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
- [Sphinx autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
- [TypeDoc](https://typedoc.org/)
- [uv: locks and syncing](https://docs.astral.sh/uv/concepts/projects/sync/)
