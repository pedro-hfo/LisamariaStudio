# Lisamaria Studio

A local learning project for a massage studio with one practitioner. Learn frontend development while building a Python backend with Domain-Driven Design (DDD), hexagonal architecture and Behaviour-Driven Development (BDD).

Projeto local de aprendizagem para um estúdio de massagens com uma profissional. Aprender desenvolvimento frontend enquanto construímos um backend Python com DDD, arquitetura hexagonal e BDD.

[Current State](#current-state) · [Toolchain](#toolchain--ferramentas) · [Project Layout](#project-layout--estrutura) · [Quick Start](#quick-start--arranque) · [Evolution](#evolution) · [Workflow](#branch-and-merge-workflow--fluxo-de-branches-e-merges)

## Current State

**Local learning foundation, with four implementation stages integrated.**
**Base local de aprendizagem, com quatro etapas de implementação integradas.**

| Area / Área | Working today / Disponível atualmente |
|---|---|
| Frontend | React booking form with loading, error and confirmation states; responsive styling and accessible controls. / Formulário React com estados de carregamento, erro e confirmação; apresentação adaptável e controlos acessíveis. |
| Backend | FastAPI appointment API; domain rules, use case, ports and adapters kept separate. / API FastAPI de marcações; regras de domínio, caso de uso, portas e adapters separados. |
| Booking / Marcação | Rejects past appointments, overlaps and conflicts with preparation time. / Rejeita marcações passadas, sobreposições e conflitos com o tempo de preparação. |
| Acceptance / Aceitação | Executable Portuguese and English Gherkin scenarios, plus Vitest component acceptance tests. / Cenários Gherkin executáveis em português e inglês, mais testes de aceitação de componentes com Vitest. |
| Documentation / Documentação | Sphinx PT/EN guides, ubiquitous language, Python autodoc and TypeDoc references, with live rebuilding. / Guias Sphinx PT/EN, linguagem ubíqua, referências Python autodoc e TypeDoc, com reconstrução automática. |
| Local workflow / Fluxo local | One command starts the application on `x` and documentation on `x+1`; Ctrl+C stops all services. / Um comando inicia a aplicação em `x` e a documentação em `x+1`; Ctrl+C termina todos os serviços. |

The demonstration uses **in-memory storage**, a **60-minute session** and a **15-minute preparation buffer**. These durations are teaching examples, not confirmed business policies. Restarting the backend clears the schedule. It does not book real appointments or charge payments.

A demonstração usa **armazenamento em memória**, uma **sessão de 60 minutos** e **15 minutos de preparação**. Estas durações são exemplos didáticos, não políticas confirmadas. Reiniciar o backend limpa a agenda. Não cria marcações reais nem cobra pagamentos.

**Not implemented yet:** permanent persistence, authentication, the real service catalogue and business policies, availability updates across clients, and SIBS payments. The current UI updates after its own requests; it does not yet receive real-time updates from other clients.

**Ainda por implementar:** persistência definitiva, autenticação, catálogo e políticas reais, atualização de disponibilidade entre clientes e pagamentos SIBS. A interface atualiza após os seus próprios pedidos; ainda não recebe atualizações em tempo real de outros clientes.

### Validation / Validação

- **21 Python tests + 4 Vitest tests pass**, including both Gherkin languages, concurrency, module boundaries and documentation parity. / **21 testes Python + 4 testes Vitest passam**, incluindo as duas línguas Gherkin, concorrência, fronteiras dos módulos e paridade da documentação.
- Frontend build, Ruff, mypy and strict Sphinx build pass. / Build frontend, Ruff, mypy e build estrito Sphinx passam.
- Launcher startup/shutdown and live guide/Python/TypeScript reference updates were verified during the foundation setup; their implementation is unchanged by this commit reorganisation. / O arranque/encerramento e as atualizações automáticas dos guias e referências Python/TypeScript foram verificados na preparação da base; a implementação mantém-se nesta reorganização dos commits.

Dependency compatibility notes are recorded in [ADR-001 (EN)](docs/en/decisions/stack.md) and [ADR-001 (PT)](docs/pt/decisions/stack.md).
As notas de compatibilidade das dependências estão registadas nesses documentos.

## Toolchain / Ferramentas

| Area / Área | Tools / Ferramentas | Purpose / Objetivo |
|---|---|---|
| Interface | React + TypeScript | Components, composition and explicit contracts. / Componentes, composição e contratos explícitos. |
| Frontend development / Desenvolvimento frontend | Vite | Local server, live updates and production build. / Servidor local, atualização automática e build de produção. |
| Backend | Python 3.13 + FastAPI | Domain implementation and HTTP adapter. / Implementação do domínio e adapter HTTP. |
| Dependencies / Dependências | uv + npm | Isolated Python environment and reproducible lockfiles. / Ambiente Python isolado e lockfiles reproduzíveis. |
| Frontend tests / Testes frontend | Vitest + React Testing Library | Test observable component behaviour. / Testar comportamentos observáveis dos componentes. |
| Business acceptance / Aceitação de negócio | pytest-bdd + Gherkin | Execute PT/EN business examples. / Executar exemplos de negócio PT/EN. |
| Documentation / Documentação | Sphinx + autodoc + MyST + Furo | Learning guides and Python reference. / Guias de aprendizagem e referência Python. |
| TypeScript reference / Referência TypeScript | TypeDoc | Generate frontend reference pages for Sphinx. / Gerar páginas de referência frontend para Sphinx. |
| Python quality / Qualidade Python | Ruff + mypy | Style, static checks and types. / Estilo, verificações estáticas e tipos. |

## Project Layout / Estrutura

```text
frontend/
  src/
    App.tsx                             # Frontend composition / composição frontend
    modules/appointments/
      domain.ts                         # Types and gateway port / tipos e porta gateway
      application/useAppointments.ts    # Async coordination / coordenação assíncrona
      adapters/httpGateway.ts           # HTTP adapter
      ui/BookingPanel.tsx               # Accessible form / formulário acessível
    shared/                             # Shared utilities / utilitários partilhados
  tests/                                # Test setup / preparação dos testes
  vite.config.ts
  typedoc.json
backend/
  src/lisamaria/
    bootstrap.py                        # Composition root / ligação das dependências
    modules/appointments/
      domain.py                         # Entities and value objects / entidades e valores
      application.py                    # Use case / caso de uso
      ports.py                          # Repository and clock contracts / contratos
      adapters/                         # HTTP, memory and clock / HTTP, memória e relógio
  tests/
    modules/appointments/               # Domain and adapter tests / testes de domínio
    test_architecture.py                # Dependency boundaries / fronteiras de dependência
acceptance/
  backend/appointments/
    features/pt/                        # Portuguese Gherkin / Gherkin português
    features/en/                        # English Gherkin / Gherkin inglês
    test_booking.py                     # Shared step definitions / passos partilhados
  frontend/appointments/
    booking.test.tsx                    # Vitest + Testing Library
scripts/
  setup.py                              # Install locked dependencies / instalar dependências
  dev.py                                # Start and stop services / iniciar e terminar serviços
  check.py                              # Quality checks / verificações
  docs_generate.py                      # Generate reference pages / gerar referências
  tests/                                # Launcher and documentation / arranque e documentação
docs/
  conf.py                               # Sphinx configuration / configuração Sphinx
  pt/                                   # Portuguese guides / guias portugueses
  en/                                   # English guides / guias ingleses
  _static/                              # Documentation assets / recursos da documentação
package.json                            # Shared commands / comandos comuns
package-lock.json                       # Locked npm dependencies / dependências npm fixadas
pyproject.toml                          # Python project and tools / projeto Python e ferramentas
uv.lock                                 # Locked Python dependencies / dependências Python fixadas
```

Code, acceptance tests and guides share the `appointments` module vocabulary. Python domain/application code does not depend on HTTP or storage adapters; `bootstrap.py` wires them together. Generated references and build outputs are ignored by Git.

Código, testes de aceitação e guias partilham o vocabulário do módulo `appointments`. O domínio e a aplicação Python não dependem dos adapters HTTP ou de armazenamento; `bootstrap.py` liga-os. As referências geradas e os builds são ignorados pelo Git.

## Quick Start / Arranque

Requires Node **22.12+** (24 recommended), npm, uv and Python 3 for the installer. uv installs the project's Python 3.13 in isolation.

Requer Node **22.12+** (24 recomendado), npm, uv e Python 3 para o instalador. uv instala o Python 3.13 do projeto num ambiente isolado.

```bash
npm run setup
npm run dev -- --port 3000
```

| Address / Endereço | Service / Serviço |
|---|---|
| <http://127.0.0.1:3000> | Application / Aplicação |
| <http://127.0.0.1:3001/pt/index.html> | Portuguese documentation / Documentação portuguesa |
| <http://127.0.0.1:3001/en/index.html> | English documentation / Documentação inglesa |
| <http://127.0.0.1:3000/api/docs> | Interactive HTTP contract / Contrato HTTP interativo |

Use `--port x` for another application port; documentation runs on `x+1`. The backend uses a free internal port and is exposed through `/api`. Ctrl+C stops every service. Logs are written to `.cache/dev/<process>/`.

Usa `--port x` para outra porta da aplicação; a documentação fica em `x+1`. O backend usa uma porta interna livre e é exposto através de `/api`. Ctrl+C termina todos os serviços. Os logs ficam em `.cache/dev/<processo>/`.

### Commands / Comandos

| Command / Comando | Purpose / Objetivo |
|---|---|
| `npm run setup` | Install from lockfiles. / Instalar a partir dos lockfiles. |
| `npm run check` | Run all quality checks, tests and builds. / Executar verificações, testes e builds. |
| `npm test` | Run frontend component acceptance tests. / Executar testes de aceitação de componentes. |
| `.venv/bin/pytest acceptance/backend -v` | Run PT/EN BDD scenarios. / Executar cenários BDD PT/EN. |
| `npm run build` | Type-check and build the frontend. / Verificar tipos e construir o frontend. |
| `npm run docs:build` | Build documentation, treating warnings as errors. / Construir documentação, tratando avisos como erros. |
| `npm run dev -- --port 4100 --check` | Start, verify and stop the local services. / Iniciar, verificar e terminar os serviços locais. |

## Evolution

The foundation is organised into four implementation branches, each integrated into `main` by a descriptive **merge commit**. Documentation is brought up to date at the merge boundary. The rows below describe completed work, not planned features.

A base está organizada em quatro branches de implementação, cada uma integrada em `main` através de um **merge commit** descritivo. A documentação é atualizada no momento do merge. As linhas seguintes descrevem trabalho concluído, não funcionalidades planeadas.

| Step / Etapa | Branch · implementation commit / commit de implementação | Improvement / Melhoria | Verification / Verificação |
|---|---|---|---|
| 01 | `setup/toolchain` · `3baa3e5` | Pin runtimes, lock dependencies and add setup. / Fixar runtimes, bloquear dependências e adicionar instalação. | Python lock consistency; setup script compiles. / Consistência do lock Python; script de instalação compila. |
| 02 | `feature/appointments-api` · `987c142` | Add appointment domain, hexagonal API and PT/EN BDD. / Adicionar domínio de marcações, API hexagonal e BDD PT/EN. | 14 backend tests pass. / 14 testes backend passam. |
| 03 | `feature/booking-ui` · `c550cb7` | Add the React form, gateway, asynchronous states and responsive styling. / Adicionar formulário React, gateway, estados assíncronos e apresentação adaptável. | 4 Vitest tests and frontend build pass. / 4 testes Vitest e build frontend passam. |
| 04 | `docs/developer-workflow` · `94c43dd` | Add Sphinx PT/EN guides, code references, glossary, coordinated servers and this evolution overview. / Adicionar guias Sphinx PT/EN, referências de código, glossário, servidores coordenados e este histórico. | 7 tooling/documentation tests, Ruff, mypy and strict Sphinx build pass. / 7 testes de ferramentas/documentação, Ruff, mypy e build estrito Sphinx passam. |

### Follow the progression / Acompanhar a evolução

```bash
# Implementation details / Detalhes da implementação
git show 987c142

# Integrated milestones, including documentation / Etapas integradas, incluindo documentação
git log --first-parent --oneline main

# Explicit merges / Merges explícitos
git log --first-parent --merges --oneline main

# Branch graph / Grafo das branches
git log --graph --oneline main
```

Read the README **at each merge** for that stage's capabilities and commands. The implementation commits intentionally need not contain updated documentation. The earlier linear history is preserved on `archive/linear-foundation`; the branch-and-merge history on `main` is the current learning path.

Lê o README **em cada merge** para conhecer as capacidades e comandos dessa etapa. Os commits de implementação não precisam de conter documentação atualizada. O histórico linear anterior está preservado em `archive/linear-foundation`; o percurso atual de aprendizagem é o histórico de branches e merges em `main`.

### Next steps — planned / Próximas etapas — planeadas

1. Confirm services, prices, session durations and preparation/cancellation policies. / Confirmar serviços, preços, durações e políticas de preparação/cancelamento.
2. Add permanent storage and protected studio administration. / Adicionar armazenamento definitivo e administração protegida.
3. Implement shared live availability for the single practitioner. / Implementar disponibilidade partilhada em tempo real para a única profissional.
4. Integrate configurable SIBS sandbox payments and payment-status handling. / Integrar pagamentos configuráveis no sandbox SIBS e tratamento dos estados de pagamento.

## Branch and Merge Workflow / Fluxo de branches e merges

Create a branch for each step. Make descriptive, focused implementation commits. Only integration into `main` requires the affected documentation and the README's **Evolution** and **Current State** sections to be current.

Cria uma branch para cada etapa. Faz commits de implementação descritivos e focados. Só a integração em `main` exige que a documentação afetada e as secções **Evolution** e **Current State** do README estejam atualizadas.

```bash
git switch main
git switch -c feature/<step>
# Implement and commit focused changes / Implementar e fazer commits focados
git add <changed-files>
git commit -m "feat(<module>): describe the observable improvement"

git switch main
git merge --no-ff --no-commit feature/<step>
# Update README and affected PT/EN docs / Atualizar README e documentação PT/EN
# Run the checks appropriate to the change / Executar as verificações adequadas
git add README.md <changed-documentation-files>
git commit -m "merge: integrate <step> and update project documentation"
```

## Learning Path / Percurso de aprendizagem

| Topic / Tema | English | Português |
|---|---|---|
| Start the project / Iniciar o projeto | [Getting started](docs/en/getting-started.md) | [Começar](docs/pt/getting-started.md) |
| Shared business vocabulary / Vocabulário comum | [Ubiquitous language](docs/en/glossary.md) | [Linguagem ubíqua](docs/pt/glossary.md) |
| DDD and hexagonal architecture / DDD e arquitetura hexagonal | [Architecture](docs/en/architecture.md) | [Arquitetura](docs/pt/architecture.md) |
| React patterns / Padrões React | [Frontend module](docs/en/modules/frontend.md) | [Módulo frontend](docs/pt/modules/frontend.md) |
| BDD and acceptance / BDD e aceitação | [Acceptance guide](docs/en/acceptance/appointments.md) | [Guia de aceitação](docs/pt/acceptance/appointments.md) |
| Documentation depth / Profundidade da documentação | [Documentation guide](docs/en/documentation.md) | [Guia de documentação](docs/pt/documentation.md) |
