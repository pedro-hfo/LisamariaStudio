# Lisamaria Studio

A local learning project for a massage studio with one practitioner.
Projeto local de aprendizagem para um estúdio de massagens com uma profissional.

## Current State

**Stage / Etapa 1 of / de 4 — Reproducible workspace / Workspace reproduzível.**

This commit contains the capabilities listed below. Later stages are not available yet.
Este commit contém as capacidades abaixo. As etapas posteriores ainda não estão disponíveis.

- **Reproducible workspace / Workspace reproduzível:** Pin runtimes, lock dependencies, create the Python package and provide a setup command. Fixar runtimes, bloquear dependências, criar o pacote Python e disponibilizar a instalação.

## Toolchain / Ferramentas

| Area / Área | Tools / Ferramentas |
|---|---|
| Frontend | React · TypeScript · Vite |
| Backend | Python 3.13 · FastAPI · uv |
| Frontend tests / Testes frontend | Vitest · React Testing Library |
| Business acceptance / Aceitação de negócio | pytest-bdd · Gherkin PT/EN |
| Documentation / Documentação | Sphinx · autodoc · MyST · Furo · TypeDoc |

## Setup / Instalação

Requires Node 22.12+ (24 recommended), npm, uv and Python 3 for the installer.
Requer Node 22.12+ (24 recomendado), npm, uv e Python 3 para o instalador.

```bash
npm run setup
```

The installer uses the committed lockfiles. / O instalador usa os lockfiles versionados.

The application is not implemented at this stage. The next commit adds the backend.
A aplicação ainda não está implementada nesta etapa. O próximo commit adiciona o backend.

## Project Layout / Estrutura

```text
frontend/       # React workspace / workspace React
backend/        # Python package / pacote Python
scripts/        # Development tooling / ferramentas de desenvolvimento
```

## Evolution

The existing foundation is being organised into progressive, reviewable commits.
A base existente está a ser organizada em commits progressivos e fáceis de rever.

| Step / Etapa | Commit | Improvement / Melhoria |
|---|---|---|
| 01 | `this commit / este commit` | **Reproducible workspace / Workspace reproduzível** — Pin runtimes, lock dependencies, create the Python package and provide a setup command. Fixar runtimes, bloquear dependências, criar o pacote Python e disponibilizar a instalação. |

## Next / Próximo

Pending product work: real service catalogue and policies, persistence, authentication, live availability and SIBS payments.
Trabalho de produto pendente: catálogo e políticas reais, persistência, autenticação, disponibilidade em tempo real e pagamentos SIBS.
