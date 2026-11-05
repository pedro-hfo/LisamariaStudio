"""PT: Adapter de entrada HTTP; traduz JSON e erros de domínio.

EN: Inbound HTTP adapter; translates JSON and domain errors.
"""

from fastapi import APIRouter, HTTPException
from pydantic import AwareDatetime, BaseModel, ConfigDict

from ..application import BookAppointment
from ..domain import Appointment, SlotUnavailable
from ..ports import AppointmentRepository


class BookingRequest(BaseModel):
    """PT: DTO de entrada; exige um fuso horário. EN: Input DTO; requires a timezone."""

    model_config = ConfigDict(extra="forbid")
    starts_at: AwareDatetime


class AppointmentResponse(BaseModel):
    """PT: DTO público sem dados pessoais. EN: Public DTO without personal data."""

    id: str
    starts_at: AwareDatetime
    ends_at: AwareDatetime
    buffer_minutes: int

    @classmethod
    def from_domain(cls, appointment: Appointment) -> "AppointmentResponse":
        """PT: Mapeia o domínio para o contrato HTTP. EN: Map domain to HTTP contract."""
        return cls(
            id=appointment.id,
            starts_at=appointment.slot.starts_at,
            ends_at=appointment.slot.ends_at,
            buffer_minutes=appointment.buffer_minutes,
        )


def create_router(
    book_appointment: BookAppointment, repository: AppointmentRepository
) -> APIRouter:
    """PT: Injeta os casos de uso sem criar dependências globais.

    EN: Inject use cases without creating global dependencies.
    """
    router = APIRouter(prefix="/appointments", tags=["appointments / marcações"])

    @router.get("")
    def list_appointments() -> list[AppointmentResponse]:
        return [AppointmentResponse.from_domain(item) for item in repository.list_all()]

    @router.post("", status_code=201)
    def book(request: BookingRequest) -> AppointmentResponse:
        try:
            return AppointmentResponse.from_domain(book_appointment.execute(request.starts_at))
        except SlotUnavailable as error:
            raise HTTPException(409, "Horário indisponível / Time slot unavailable.") from error
        except ValueError as error:
            raise HTTPException(422, str(error)) from error

    return router
