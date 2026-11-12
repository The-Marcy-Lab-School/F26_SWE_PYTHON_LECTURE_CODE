"""Tests for the classes in events.py."""

from datetime import date, timedelta

import pytest

from events import Event, Concert, Workshop, Screening


def test_two_events_hold_separate_data():
    first = Screening('Movie Night: Up', date(2026, 12, 10), capacity=30, base_price=8)
    second = Screening('Movie Night: Moana', date(2026, 12, 17), capacity=30, base_price=8)

    first.name = 'Movie Night: Wall-E'

    assert second.name == 'Movie Night: Moana'


def test_capacity_setter_refuses_a_capacity_below_one(jazz):
    with pytest.raises(ValueError):
        jazz.capacity = 0


def test_a_refused_capacity_leaves_the_stored_value_unchanged(jazz):
    with pytest.raises(ValueError):
        jazz.capacity = -5

    assert jazz.capacity == 40


def test_creating_an_event_with_a_negative_price_is_refused():
    with pytest.raises(ValueError):
        Screening('Movie Night: Up', date(2026, 12, 10), capacity=30, base_price=-1)


def test_each_kind_of_event_prices_its_tickets_differently(jazz, pottery, spirited_away):
    assert jazz.ticket_price() == 30            # 25 plus the 5 service fee
    assert pottery.ticket_price() == 25         # 15 plus the 10 materials fee
    assert spirited_away.ticket_price() == 8    # the base price, unchanged


def test_each_kind_of_event_has_its_own_refund_rule(jazz, pottery, spirited_away):
    eight_days = timedelta(days=8)
    one_day = timedelta(days=1)

    assert jazz.can_refund(jazz.date - eight_days) is True
    assert pottery.can_refund(pottery.date - eight_days) is True
    assert spirited_away.can_refund(spirited_away.date - eight_days) is False

    assert jazz.can_refund(jazz.date - one_day) is False
    assert pottery.can_refund(pottery.date - one_day) is False


def test_the_plain_event_refunds_until_the_day_before():
    event = Event('Open Mic', date(2026, 12, 10), capacity=20, base_price=0)

    assert event.can_refund(date(2026, 12, 9)) is True
    assert event.can_refund(date(2026, 12, 10)) is False


def test_repr_names_the_kind_of_event(jazz, pottery):
    assert repr(jazz) == "Concert('Friday Night Jazz', 2026-12-13)"
    assert repr(pottery) == "Workshop('Intro to Pottery', 2026-12-05)"


def test_two_events_with_the_same_name_and_date_are_equal(jazz):
    jazz_again = Concert('Friday Night Jazz', jazz.date, capacity=60, base_price=30,
                         performer='The Blue Notes')

    assert jazz_again == jazz
    assert jazz_again is not jazz


def test_events_on_different_dates_are_not_equal(jazz):
    next_week = Concert('Friday Night Jazz', jazz.date + timedelta(days=7), capacity=40,
                        base_price=25, performer='The Blue Notes')

    assert next_week != jazz


def test_one_loop_prices_every_kind_of_event(venue):
    prices = [event.ticket_price() for event in venue.events]

    assert prices == [30, 25, 8, 8]


def test_a_concert_and_a_workshop_keep_their_own_extra_attribute(jazz, pottery):
    assert jazz.performer == 'The Blue Notes'
    assert pottery.materials_fee == 10
    assert isinstance(jazz, Concert)
    assert isinstance(pottery, Workshop)
