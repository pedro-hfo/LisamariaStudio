"""PT: Composition root: o único local que liga portas a adapters concretos.

EN: Composition root: the place that wires ports to concrete adapters.
"""

from fastapi import FastAPI

from .modules.appointments.adapters.http import create_router
from .modules.appointments.adapters.memory import InMemoryAppointmentRepository
from .modules.appointments.adapters.system_clock import SystemClock
from .modules.appointments.application import BookAppointment
from .modules.appointments.ports import Clock


def create_app(clock: Clock | None = None) -> FastAPI:
    """PT: Cria uma aplicação isolada por execução ou teste.

    EN: Create an isolated application for each run or test.
    """
    app = FastAPI(
        title="Lisamaria Studio · Local learning API",
        version="0.1.0",
        description="PT: Exemplo local, sem pagamentos. EN: Local example, no payments.",
        docs_url="/api/docs",
        redoc_url=None,
        openapi_url="/api/openapi.json",
    )
    repository = InMemoryAppointmentRepository()
    use_case = BookAppointment(repository, clock if clock is not None else SystemClock())
    app.include_router(create_router(use_case, repository), prefix="/api")

    @app.get("/api/health", tags=["system"])
    def health() -> dict[str, str]:
        return {"status": "ok", "mode": "local-demo"}

    return app
