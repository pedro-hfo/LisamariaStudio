"""PT: Contratos de saída exigidos pelo caso de uso.

EN: Outbound contracts required by the use case.
"""

from datetime import datetime
from typing import Protocol

from .domain import Appointment


class AppointmentRepository(Protocol):
    """PT: Porta que exige verificação e gravação atómicas de uma marcação.

    EN: Port requiring atomic conflict checking and appointment storage.
    """

    def add_if_available(self, appointment: Appointment) -> None:
        """PT: Grava ou lança SlotUnavailable, sem uma janela de concorrência.

        EN: Save or raise SlotUnavailable, without a concurrency gap.
        """
        ...

    def list_all(self) -> list[Appointment]:
        """PT: Devolve marcações ordenadas por início.

        EN: Return appointments ordered by start time.
        """
        ...


class Clock(Protocol):
    """PT: Porta para controlar o tempo nos testes.

    EN: Port allowing time to be controlled in tests.
    """

    def now(self) -> datetime:
        """PT: Instante atual com fuso horário. EN: Current timezone-aware instant."""
        ...
