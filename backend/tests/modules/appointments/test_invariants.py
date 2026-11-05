from concurrent.futures import ThreadPoolExecutor
from datetime import UTC, datetime, timedelta

import pytest
from lisamaria.modules.appointments.adapters.memory import InMemoryAppointmentRepository
from lisamaria.modules.appointments.domain import Appointment, SlotUnavailable, TimeSlot


def test_only_one_concurrent_booking_is_accepted():
    repository = InMemoryAppointmentRepository()
    start = datetime(2030, 1, 10, 10, tzinfo=UTC)

    def book(identifier):
        try:
            repository.add_if_available(
                Appointment(str(identifier), TimeSlot(start, start + timedelta(hours=1)))
            )
            return True
        except SlotUnavailable:
            return False

    with ThreadPoolExecutor(max_workers=8) as executor:
        assert sum(executor.map(book, range(32))) == 1
    assert len(repository.list_all()) == 1


def test_timezone_is_required():
    with pytest.raises(ValueError, match="timezone"):
        TimeSlot(datetime(2030, 1, 1), datetime(2030, 1, 1, 1))


def test_end_must_follow_start():
    start = datetime(2030, 1, 1, tzinfo=UTC)
    with pytest.raises(ValueError, match="End"):
        TimeSlot(start, start)
