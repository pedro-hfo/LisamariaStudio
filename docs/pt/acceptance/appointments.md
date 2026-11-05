# Aceitação: marcações

BDD significa **Behaviour-Driven Development**: primeiro descobrimos o comportamento em conjunto, depois formulamos exemplos e, por fim, automatizamos. Gherkin é a notação, não o processo inteiro.

## Ciclo de trabalho

1. **Discovery:** que regra queremos? Que exemplos e dúvidas existem?
2. **Formulation:** escreve `Dado / Quando / Então` com a linguagem do negócio.
3. **Automation:** liga os passos à interface pública do módulo.
4. Faz o cenário falhar pela razão esperada; implementa; volta a executar.
5. Atualiza PT e EN, mantendo os mesmos IDs e os mesmos exemplos.

## Estrutura paralela

| Código | Aceitação | Documentação |
|---|---|---|
| `backend/src/lisamaria/modules/appointments/` | `acceptance/backend/appointments/` | `docs/pt/modules/appointments.md` |
| `frontend/src/modules/appointments/` | `acceptance/frontend/appointments/` | `docs/pt/modules/frontend.md` |

No backend, os ficheiros `features/pt/` e `features/en/` são ambos executáveis com pytest-bdd. Partilham as implementações de passos em `test_booking.py`. O relógio é fixo para os cenários não ficarem obsoletos com o tempo.

No front-end, os testes de aceitação de componentes são escritos em Vitest + Testing Library, com títulos bilingues e IDs estáveis. Não os apresentamos como testes de navegador completos: usam jsdom e uma porta substituta.

## Rastreabilidade

| ID | Comportamento | Verificação |
|---|---|---|
| APT-001 | Aceitar um horário livre | Gherkin PT/EN → HTTP real em processo |
| APT-002 | Rejeitar sobreposição | Gherkin PT/EN |
| APT-003 | Preservar preparação | Gherkin PT/EN |
| APT-004 | Permitir após preparação | Gherkin PT/EN |
| APT-005 | Rejeitar passado | Gherkin PT/EN |
| UI-001 | Mostrar confirmação | Vitest + Testing Library |
| UI-002 | Explicar indisponibilidade | Vitest + Testing Library |
| UI-003 | Impedir submissão repetida | Vitest + Testing Library |
| UI-004 | Comunicar erro de carregamento | Vitest + Testing Library |

Os testes unitários cobrem também concorrência e intervalos inválidos. A verificação de traduções compara IDs e estrutura; a equivalência do significado exige revisão humana.

```{hint}
*Given / When / Then* corresponde a **Dado / Quando / Então**. Escreve uma intenção observável, por exemplo «o horário está indisponível», em vez de «a função devolve False».
```

[Cenários incluídos diretamente dos ficheiros executáveis](../reference/generated/scenarios.rst)
