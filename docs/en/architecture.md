# Architecture, one part at a time

## The essential idea

The rule “one practitioner cannot have overlapping appointments” belongs to the business. It should be testable without a browser, HTTP server or database.

**DDD — Domain-Driven Design** shapes the model around business language and rules. **Hexagonal architecture** connects that model to technology through contracts called *ports* and implementations called *adapters*.

```text
BookingPanel → useAppointments → AppointmentGateway
                                      ↓ HTTP adapter
                               POST /api/appointments
                                      ↓ HTTP adapter
                               BookAppointment
                                 ↓         ↓
                              domain     ports
                                           ↑
                                  concrete adapters
```

Dependencies point inward: adapters know ports and the domain. The domain does not know adapters. `bootstrap.py` connects them: the *composition root*.

## Patterns in use

| Pattern | Where | Why it exists |
|---|---|---|
| Value object | `TimeSlot` | Compares intervals by value and prevents invalid intervals |
| Entity | `Appointment` | Maintains its own identity through an ID |
| Use case | `BookAppointment` | Coordinates a complete user intention |
| Port / interface | `AppointmentRepository`, `Clock` | Defines what the use case needs |
| Adapter | memory, clock, HTTP | Connects contracts to concrete technologies |
| Dependency injection | constructors and `bootstrap.py` | Swaps collaborators without changing rules |
| Composition | `BookingPanel` receives `gateway` | Makes components reusable and testable |
| Custom hook | `useAppointments` | Separates asynchronous coordination from presentation |

```{hint}
In Portuguese, *port* means **porta/contrato** here, not a TCP port. *Adapter* means **adaptador**. We retain English identifiers to make the literature easier to search.
```

## Grow when needed

We start with a modular monolith. The `appointments` module is an initial business boundary; we do not yet claim it is the final bounded context. Domain and application files will be split when distinct concepts justify it.

Future persistence must guarantee schedule exclusion inside the database transaction itself. The current lock protects only one demonstration process. SIBS will enter through a payment port; the domain should not import its SDK or payloads.

This foundation has no domain events, CQRS or microservices. Those will be decisions driven by concrete needs and recorded in ADRs.
