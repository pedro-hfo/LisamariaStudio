"""PT: Regras de marcação sem dependências de frameworks.

EN: Appointment rules without framework dependencies.
"""

from dataclasses import dataclass
from datetime import datetime, timedelta


class SlotUnavailable(Exception):
    """PT: O horário e o intervalo de preparação já estão ocupados.

    EN: The time slot or its preparation buffer is already occupied.
    """


@dataclass(frozen=True)
class TimeSlot:
    """PT: Value object que representa um intervalo com fuso horário.

    EN: Value object representing a timezone-aware interval.
    """

    starts_at: datetime
    ends_at: datetime

    def __post_init__(self) -> None:
        if any(value.utcoffset() is None for value in (self.starts_at, self.ends_at)):
            raise ValueError("A timezone is required / É necessário um fuso horário.")
        if self.ends_at <= self.starts_at:
            raise ValueError("End must follow start / O fim deve ser posterior ao início.")

    def overlaps(self, other: "TimeSlot") -> bool:
        """PT: Intervalos adjacentes não se sobrepõem: usamos [início, fim).

        EN: Adjacent intervals do not overlap: we use [start, end).
        """
        return self.starts_at < other.ends_at and other.starts_at < self.ends_at


@dataclass(frozen=True)
class Appointment:
    """PT: Entidade identificada por ID; reserva tempo de uma profissional.

    EN: Entity identified by ID; reserves one practitioner's time.
    """

    id: str
    slot: TimeSlot
    buffer_minutes: int = 15

    def __post_init__(self) -> None:
        if self.buffer_minutes < 0:
            raise ValueError("Buffer cannot be negative / O intervalo não pode ser negativo.")

    @property
    def occupied_slot(self) -> TimeSlot:
        """PT: Sessão mais o intervalo de preparação no final.

        EN: Session plus the preparation buffer at the end.
        """
        return TimeSlot(
            self.slot.starts_at, self.slot.ends_at + timedelta(minutes=self.buffer_minutes)
        )
