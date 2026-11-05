# Frontend: components and behaviours

## The tools

- **React:** component library for building the interface.
- **TypeScript:** types that make contracts explicit.
- **Vite:** frontend development server and build tool.
- **Vitest:** runs tests and reports results.
- **React Testing Library:** finds fields and buttons and observes the interface in tests.
- **TypeDoc:** turns comments and types into a code reference.

## Organisation by feature

```text
frontend/src/modules/appointments/
  domain.ts                    # types and port
  application/useAppointments.ts
  adapters/httpGateway.ts
  ui/BookingPanel.tsx

acceptance/frontend/appointments/
  booking.test.tsx
```

The component receives `AppointmentGateway`. The hook manages loading, errors, submission and confirmation. The adapter knows `fetch` and HTTP DTOs. The component knows visual elements and interactions.

We do not need to reproduce every backend layer. Authoritative business rules remain in Python; React owns interface responsibilities.

## Robustness and presentation

Asynchronous states are explicit. There are labels, visible focus, `role=alert/status` messages and protection against repeat submission. Tests use these public elements instead of React internals.

CSS starts with colour, border and typography tokens in `styles.css`. Components use composition without deep inheritance. The grid adapts to mobile. Remote fonts have local fallbacks; the application works without downloading them.

**Hint:** *composition* is **composição** in Portuguese: building larger components from smaller ones. A *hook* encapsulates reusable React logic; it is not a mandatory layer for every function.

## Next exercise

Read `UI-002`. Change the conflict message, update the expectation and run `npm test`. Then adjust spacing and compare the narrow page layout. Automated tests do not assess aesthetic quality.
