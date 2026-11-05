# Lisamaria Studio

A learning project for a massage studio with one practitioner.
Projeto de aprendizagem para um estúdio de massagens com uma profissional.

## Current State

Project scope and Git workflow are defined. Implementation will arrive through feature branches.
O âmbito do projeto e o fluxo Git estão definidos. A implementação será integrada através de branches.

## Planned Layout / Estrutura prevista

```text
frontend/    # React + TypeScript
backend/     # Python + FastAPI, DDD and hexagonal architecture
acceptance/  # Tests mirroring business modules / testes paralelos aos módulos
scripts/     # Development tooling / ferramentas de desenvolvimento
docs/pt/     # Portuguese documentation / documentação portuguesa
docs/en/     # English documentation / documentação inglesa
```

## Evolution

This initial commit records the project scope. No application capability has been merged yet.
Este commit inicial regista o âmbito. Ainda não foi integrada nenhuma capacidade da aplicação.

1. Reproducible toolchain / Ferramentas reproduzíveis.
2. Appointment domain and API / Domínio de marcações e API.
3. React booking interface / Interface React de marcações.
4. Bilingual documentation and local servers / Documentação bilingue e servidores locais.

These steps are planned, not completed. / Estas etapas estão planeadas, não concluídas.

## Commit and Merge Workflow / Fluxo de commits e merges

Use a named branch for each step and descriptive implementation commits. Integrate with an explicit merge commit. Update Evolution, Current State and affected documentation as part of the merge; intermediate branch commits do not need fully updated documentation.

Usa uma branch com nome para cada etapa e commits de implementação descritivos. Integra com um merge commit explícito. Atualiza Evolution, Current State e a documentação afetada no merge; os commits intermédios da branch não precisam de ter toda a documentação atualizada.
