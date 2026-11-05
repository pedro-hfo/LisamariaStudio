# Lisamaria Studio

This repository is a massage studio website, independent of the parent German-learning project.
Follow `/Users/pedrofonseca/.codex/RTK.md` when available.

- Keep work local unless publication is explicitly requested.
- Frontend: React, TypeScript, Vite, Vitest and React Testing Library.
- Backend: Python, FastAPI, DDD and hexagonal architecture; business modules live under `backend/src/lisamaria/modules/`.
- Domain and application must not import adapters or web frameworks. Wire dependencies in `bootstrap.py`.
- Acceptance tests mirror business modules under `acceptance/backend/` and `acceptance/frontend/`.
- Keep PT/EN guide paths and scenario IDs aligned. Use the ubiquitous language in `docs/pt/glossary.md` and `docs/en/glossary.md`.
- Explain patterns progressively: intent and example first, detailed references second.
- Develop each step on a named branch with focused, descriptive implementation commits. Integrate into `main` with an explicit merge commit (`--no-ff`).
- Up-to-date documentation is required at the merge boundary, not for every intermediate branch commit. Prepare the merge with `--no-commit`, update the affected PT/EN documentation and README, then create the merge commit.
- Maintain the README's `Evolution` section with completed improvements and verifiable commit references, and its `Current State` section with working capabilities, validation and outstanding work. Keep planned work separate from completed work and maintain PT/EN descriptions.
- Python references use Sphinx autodoc; frontend references use TypeDoc integrated into Sphinx. Do not edit generated reference files.
- Use `npm run check` for changes across layers; use focused tests for smaller changes.
- Keep example policies clearly identified until the studio owner confirms them.
- Never commit credentials, `.env`, runtime data or generated dependency directories.
