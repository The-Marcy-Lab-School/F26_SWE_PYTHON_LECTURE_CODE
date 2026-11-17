from datetime import date

import pytest
from events import Concert, Event


def test_an_event_itself_cannot_be_created():
    with pytest.raises(TypeError):
        Event('Open Mic', date(2026, 12, 10), capacity=20, base_price=0)


def test_a_kind_of_event_missing_can_refund_cannot_be_created():
    class Festival(Event):
        def ticket_price(self):
            return super().ticket_price()

    with pytest.raises(TypeError):
        Festival('Summer Festival', date(2026, 12, 10), capacity=500, base_price=40)


def test_a_complete_kind_of_event_can_be_created():
    jazz = Concert('Friday Night Jazz', date(2026, 12, 5), capacity=40, base_price=25, performer='The Blue Notes')

    assert jazz.ticket_price() == 30
