# Ubiquitous language / Linguagem ubíqua

We use the same concepts in conversations, scenarios and modules. Code identifiers are English; guides and scenarios exist in PT and EN.

| Português | English / code | Meaning |
|---|---|---|
| Profissional | Practitioner | The single person providing massages |
| Marcação | Appointment | Reservation of an interval for a session |
| Horário | TimeSlot | Timezone-aware start and end instants |
| Sessão | Session | Time spent on the massage |
| Preparação | Preparation buffer | Occupied time after the session |
| Horário indisponível | SlotUnavailable | Conflict with an existing session or buffer |
| Marcar | BookAppointment | Intention to create an appointment |
| Agenda | Schedule | The practitioner's appointments |
| Pagamento | Payment | Planned concept; not implemented yet |

**Hint:** “booking” is the action/process; “appointment” is the resulting reservation. We avoid “event” for an individual massage session.

IDs such as `APT-001` and `UI-001` stay stable across translations. A terminology change should update the glossary, code, scenarios and both guides.
