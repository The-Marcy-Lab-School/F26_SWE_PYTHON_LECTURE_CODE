"""Tests for events_abc.py, the abstract base class version of the events."""

from datetime import date

import pytest

from events_abc import Event, Concert, Screening


def test_an_event_itself_cannot_be_created():
    with pytest.raises(TypeError):
        Event('Open Mic', date(2026, 12, 10), capacity=20, base_price=0)


def test_a_kind_of_event_missing_a_method_cannot_be_created():
    class Festival(Event):
        def ticket_price(self):
            return super().ticket_price()

    with pytest.raises(TypeError):
        Festival('Summer Festival', date(2026, 12, 10), capacity=500, base_price=40)


def test_the_abc_events_behave_like_the_plain_ones():
    concert = Concert('Friday Night Jazz', date(2026, 12, 13), 40, 25, 'The Blue Notes')
    screening = Screening('Movie Night: Up', date(2026, 12, 10), 30, 8)

    assert concert.ticket_price() == 30
    assert screening.ticket_price() == 8
    assert screening.can_refund(date(2026, 12, 1)) is False
