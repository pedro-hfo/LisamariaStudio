# Lisamaria Studio

A local learning project for a massage studio with one practitioner.
Projeto local de aprendizagem para um estúdio de massagens com uma profissional.

## Current State

**Stage / Etapa 2 of / de 4 — Business rules and HTTP API / Regras de negócio e API HTTP.**

This commit contains the capabilities listed below. Later stages are not available yet.
Este commit contém as capacidades abaixo. As etapas posteriores ainda não estão disponíveis.

- **Reproducible workspace / Workspace reproduzível:** Pin runtimes, lock dependencies, create the Python package and provide a setup command. Fixar runtimes, bloquear dependências, criar o pacote Python e disponibilizar a instalação.
- **Business rules and HTTP API / Regras de negócio e API HTTP:** Add the appointment domain, ports, adapters and executable PT/EN acceptance scenarios. Adicionar domínio de marcações, portas, adapters e cenários de aceitação executáveis PT/EN.

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

## Backend / Backend

```bash
.venv/bin/uvicorn lisamaria.bootstrap:create_app --factory --port 8000
.venv/bin/pytest backend/tests acceptance/backend -v
```

API reference / Referência API: <http://127.0.0.1:8000/api/docs>.

The example reserves 60 minutes plus a 15-minute buffer, using in-memory storage.
O exemplo reserva 60 minutos mais 15 de preparação, com armazenamento em memória.
These are teaching values, not confirmed studio policies. Restarting the backend clears the schedule.
São valores didáticos, não políticas confirmadas do estúdio. Reiniciar o backend limpa a agenda.

## Project Layout / Estrutura

```text
frontend/       # React workspace / workspace React
backend/        # Python package / pacote Python
  src/lisamaria/modules/appointments/
  tests/modules/appointments/
acceptance/backend/appointments/
scripts/        # Development tooling / ferramentas de desenvolvimento
```

## Evolution

The existing foundation is being organised into progressive, reviewable commits.
A base existente está a ser organizada em commits progressivos e fáceis de rever.

| Step / Etapa | Commit | Improvement / Melhoria |
|---|---|---|
| 01 | `3a4e26f` | **Reproducible workspace / Workspace reproduzível** — Pin runtimes, lock dependencies, create the Python package and provide a setup command. Fixar runtimes, bloquear dependências, criar o pacote Python e disponibilizar a instalação. |
| 02 | `this commit / este commit` | **Business rules and HTTP API / Regras de negócio e API HTTP** — Add the appointment domain, ports, adapters and executable PT/EN acceptance scenarios. Adicionar domínio de marcações, portas, adapters e cenários de aceitação executáveis PT/EN. |

## Next / Próximo

Pending product work: real service catalogue and policies, persistence, authentication, live availability and SIBS payments.
Trabalho de produto pendente: catálogo e políticas reais, persistência, autenticação, disponibilidade em tempo real e pagamentos SIBS.
