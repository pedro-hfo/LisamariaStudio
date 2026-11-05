# Front-end: componentes e comportamentos

## As ferramentas

- **React:** biblioteca de componentes para construir a interface.
- **TypeScript:** tipos para tornar os contratos explícitos.
- **Vite:** servidor de desenvolvimento e build do front-end.
- **Vitest:** executa testes e apresenta resultados.
- **React Testing Library:** encontra campos e botões e observa a interface nos testes.
- **TypeDoc:** transforma comentários e tipos em referência de código.

## Organização por funcionalidade

```text
frontend/src/modules/appointments/
  domain.ts                    # tipos e porta
  application/useAppointments.ts
  adapters/httpGateway.ts
  ui/BookingPanel.tsx

acceptance/frontend/appointments/
  booking.test.tsx
```

O componente recebe `AppointmentGateway`. O hook gere loading, erro, submissão e confirmação. O adapter conhece `fetch` e os DTOs HTTP. O componente conhece os elementos visuais e as interações.

Não precisamos de reproduzir todas as camadas do backend. Mantemos regras de negócio autoritativas em Python e apenas as responsabilidades de interface no React.

## Robustez e apresentação

Os estados assíncronos são explícitos. Há labels, foco visível, mensagens com `role=alert/status` e bloqueio de submissão repetida. Os testes usam esses elementos públicos em vez de detalhes internos do React.

O CSS começa com tokens de cor, bordas e tipografia em `styles.css`. Os componentes são compostos, sem heranças profundas. A grelha adapta-se ao telemóvel. As fontes remotas têm alternativas locais; a aplicação funciona sem as descarregar.

**Hint:** *composition* significa **composição**: construir componentes maiores juntando componentes menores. Um *hook* encapsula lógica React reutilizável; não é uma camada obrigatória para todas as funções.

## Próximo exercício

Lê `UI-002`. Muda a mensagem de conflito, ajusta a expectativa e executa `npm test`. Depois altera um espaçamento e compara a versão estreita da página. Testes automáticos não avaliam a qualidade estética.
