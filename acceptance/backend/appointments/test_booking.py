"""PT: As duas línguas executam os mesmos passos. EN: Both languages run the same steps."""

from datetime import UTC, datetime

import pytest
from fastapi.testclient import TestClient
from lisamaria.bootstrap import create_app
from pytest_bdd import given, parsers, scenarios, then, when

scenarios("features/en/book_appointment.feature", "features/pt/book_appointment.feature")


class FixedClock:
    def now(self):
        return datetime(2030, 1, 1, tzinfo=UTC)


@pytest.fixture
def client():
    with TestClient(create_app(FixedClock())) as client:
        yield client


@given("the practitioner has an empty schedule")
@given("que a profissional tem a agenda vazia")
def empty_schedule(client):
    assert client.get("/api/appointments").json() == []


@given(parsers.parse('an appointment starts at "{starts_at}"'))
@given(parsers.parse('que existe uma marcação às "{starts_at}"'))
def existing_appointment(client, starts_at):
    assert client.post("/api/appointments", json={"starts_at": starts_at}).status_code == 201


@when(parsers.parse('I request an appointment at "{starts_at}"'), target_fixture="response")
@when(parsers.parse('peço uma marcação às "{starts_at}"'), target_fixture="response")
def request_booking(client, starts_at):
    return client.post("/api/appointments", json={"starts_at": starts_at})


@then("the appointment is accepted")
@then("a marcação é aceite")
def accepted(response):
    assert response.status_code == 201


@then("the time slot is unavailable")
@then("o horário está indisponível")
def unavailable(response):
    assert response.status_code == 409


@then("the request is invalid")
@then("o pedido é inválido")
def invalid(response):
    assert response.status_code == 422


@then(parsers.parse("the schedule contains {count:d} appointment"))
@then(parsers.parse("the schedule contains {count:d} appointments"))
@then(parsers.parse("a agenda contém {count:d} marcação"))
@then(parsers.parse("a agenda contém {count:d} marcações"))
def appointment_count(client, count):
    assert len(client.get("/api/appointments").json()) == count
