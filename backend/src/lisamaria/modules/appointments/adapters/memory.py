"""PT: Persistência em memória apenas para a demonstração local.

EN: In-memory persistence for the local demonstration only.
"""

from threading import Lock

from ..domain import Appointment, SlotUnavailable


class InMemoryAppointmentRepository:
    """PT: Adapter com exclusão mútua dentro de um único processo.

    EN: Adapter with mutual exclusion inside a single process.
    """

    def __init__(self) -> None:
        self._appointments: list[Appointment] = []
        self._lock = Lock()

    def add_if_available(self, appointment: Appointment) -> None:
        """PT: Verifica conflitos e grava sob o mesmo lock.

        EN: Check conflicts and store under the same lock.
        """
        with self._lock:
            if any(
                existing.occupied_slot.overlaps(appointment.occupied_slot)
                for existing in self._appointments
            ):
                raise SlotUnavailable
            self._appointments.append(appointment)

    def list_all(self) -> list[Appointment]:
        """PT: Devolve uma cópia ordenada. EN: Return a sorted copy."""
        with self._lock:
            return sorted(self._appointments, key=lambda appointment: appointment.slot.starts_at)
