# Module: appointments

## Responsibility

Reserve the only practitioner's time while rejecting overlaps. This example does not manage opening hours, customers or payments.

| File under `backend/src/lisamaria/modules/appointments/` | Responsibility |
|---|---|
| `domain.py` | Valid intervals, entity and conflict error |
| `application.py` | `BookAppointment` use case |
| `ports.py` | Repository and clock contracts |
| `adapters/memory.py` | Atomic conflict check and storage in memory |
| `adapters/system_clock.py` | UTC clock |
| `adapters/http.py` | Input validation and HTTP translation |

## Reading path

1. Read `TimeSlot.overlaps`: adjacent intervals are valid.
2. Read `Appointment.occupied_slot`: it adds preparation time.
3. Read `BookAppointment.execute`: it validates and requests an atomic write.
4. Read `add_if_available`: conflict checking and writing share the same lock.
5. Read scenario `APT-003`: booking during preparation is rejected.

The server enforces the rule. Disabling a button improves the interface but does not prevent concurrent requests.

## Contract

`POST /api/appointments` accepts `starts_at` as timezone-aware ISO 8601. It returns `201` when accepted, `409` on conflict and `422` for invalid requests. `GET /api/appointments` returns the demonstration schedule.

Tests live under `backend/tests/modules/appointments/` and `acceptance/backend/appointments/`. Sphinx generates the reference from this module's docstrings.
