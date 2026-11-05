# Acceptance: appointments

BDD means **Behaviour-Driven Development**: first discover behaviour together, then formulate examples, then automate. Gherkin is the notation, not the entire process.

## Working cycle

1. **Discovery:** which rule do we want? What examples and questions do we have?
2. **Formulation:** write `Given / When / Then` using business language.
3. **Automation:** connect steps to the module's public interface.
4. Make the scenario fail for the expected reason; implement; run again.
5. Update PT and EN, retaining the same IDs and examples.

## Parallel structure

| Code | Acceptance | Documentation |
|---|---|---|
| `backend/src/lisamaria/modules/appointments/` | `acceptance/backend/appointments/` | `docs/en/modules/appointments.md` |
| `frontend/src/modules/appointments/` | `acceptance/frontend/appointments/` | `docs/en/modules/frontend.md` |

Backend files under `features/pt/` and `features/en/` are both executable with pytest-bdd. They share step implementations in `test_booking.py`. The clock is fixed so scenarios do not become outdated as time passes.

Frontend component acceptance tests use Vitest + Testing Library, with bilingual titles and stable IDs. These are not full browser tests: they use jsdom and a substitute port.

## Traceability

| ID | Behaviour | Verification |
|---|---|---|
| APT-001 | Accept an available time slot | PT/EN Gherkin → real HTTP adapter in process |
| APT-002 | Reject overlap | PT/EN Gherkin |
| APT-003 | Preserve preparation | PT/EN Gherkin |
| APT-004 | Allow booking after preparation | PT/EN Gherkin |
| APT-005 | Reject the past | PT/EN Gherkin |
| UI-001 | Show confirmation | Vitest + Testing Library |
| UI-002 | Explain unavailability | Vitest + Testing Library |
| UI-003 | Prevent repeat submission | Vitest + Testing Library |
| UI-004 | Report loading errors | Vitest + Testing Library |

Unit tests also cover concurrency and invalid intervals. Translation checks compare IDs and structure; semantic equivalence requires human review.

```{hint}
*Given / When / Then* corresponds to **Dado / Quando / Então**. Write an observable intention, such as “the time slot is unavailable”, instead of “the function returns False”.
```

[Scenarios included directly from executable files](../reference/generated/scenarios.rst)
