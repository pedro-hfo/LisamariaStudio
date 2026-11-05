"""PT: Orquestração do caso de uso de marcação.

EN: Orchestration of the booking use case.
"""

from datetime import datetime, timedelta
from uuid import uuid4

from .domain import Appointment, TimeSlot
from .ports import AppointmentRepository, Clock


class BookAppointment:
    """PT: Caso de uso de demonstração: sessão de 60 minutos e preparação de 15.

    EN: Demonstration use case: a 60-minute session and a 15-minute buffer.

    PT: Estes valores são exemplos didáticos, não uma política comercial aprovada.
    EN: These values are teaching examples, not an approved business policy.
    """

    def __init__(self, repository: AppointmentRepository, clock: Clock) -> None:
        self.repository = repository
        self.clock = clock

    def execute(self, starts_at: datetime) -> Appointment:
        """PT: Valida o início futuro e pede à porta uma gravação atómica.

        EN: Validate a future start and request an atomic write through the port.
        """
        slot = TimeSlot(starts_at, starts_at + timedelta(minutes=60))
        if starts_at <= self.clock.now():
            raise ValueError("Choose a future time / Escolhe um horário futuro.")
        appointment = Appointment(str(uuid4()), slot)
        self.repository.add_if_available(appointment)
        return appointment
