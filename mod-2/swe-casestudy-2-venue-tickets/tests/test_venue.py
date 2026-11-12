"""Tests for the Venue class, the coordinator."""

from datetime import timedelta

import pytest

from attendee import Attendee
from events import Concert
from venue import Venue


def test_the_sample_venue_starts_with_its_events_attendees_and_reservations(venue):
    assert len(venue.events) == 4
    assert len(venue.attendees) == 2
    assert len(venue.reservations) == 4


def test_upcoming_events_leaves_out_past_events_and_sorts_by_date(venue, today):
    names = [event.name for event in venue.upcoming_events(today)]

    assert names == ['Intro to Pottery', 'Friday Night Jazz', 'Movie Night: Spirited Away']


def test_find_events_keeps_only_the_events_that_match(venue):
    cheap = venue.find_events(lambda event: event.ticket_price() < 10)

    assert [event.name for event in cheap] == ['Movie Night: Spirited Away', 'Movie Night: Coco']


def test_the_events_property_returns_a_copy(venue):
    events = venue.events
    events.clear()

    assert len(venue.events) == 4


def test_is_valid_email_needs_an_at_sign_and_a_dot_after_it():
    assert Venue.is_valid_email('maya@example.com') is True
    assert Venue.is_valid_email('maya.example.com') is False
    assert Venue.is_valid_email('maya@example') is False


def test_adding_an_attendee_with_an_invalid_email_is_refused(venue):
    with pytest.raises(ValueError):
        venue.add_attendee(Attendee('Sam Park', 'sam.example.com'))

    assert len(venue.attendees) == 2


def test_adding_an_already_registered_email_is_refused(venue, capsys):
    result = venue.add_attendee(Attendee('Maya R.', 'maya@example.com'))

    assert result is None
    assert len(venue.attendees) == 2
    assert capsys.readouterr().out == 'maya@example.com is already registered.\n'


def test_adding_an_event_already_on_the_calendar_is_refused(venue, jazz, capsys):
    jazz_again = Concert('Friday Night Jazz', jazz.date, capacity=40, base_price=25,
                         performer='The Blue Notes')

    result = venue.add_event(jazz_again)

    assert result is None
    assert len(venue.events) == 4
    assert capsys.readouterr().out == f'Friday Night Jazz on {jazz.date} is already on the calendar.\n'


def test_booking_adds_a_reservation(venue, jordan, jazz, today):
    reservation = venue.book(jordan, jazz, today)

    assert reservation in venue.reservations
    assert venue.seats_left(jazz) == 38


def test_booking_a_sold_out_event_is_refused_and_changes_nothing(venue, jordan, pottery, today, capsys):
    reservations_before = venue.reservations

    result = venue.book(jordan, pottery, today)

    assert result is None
    assert venue.reservations == reservations_before
    assert capsys.readouterr().out == 'Intro to Pottery is sold out.\n'


def test_booking_an_event_that_has_already_happened_is_refused(venue, jordan, coco, today, capsys):
    result = venue.book(jordan, coco, today)

    assert result is None
    assert len(venue.reservations) == 4
    assert capsys.readouterr().out == 'Movie Night: Coco has already happened.\n'


def test_a_refund_inside_the_window_frees_the_seat(venue, maya, jazz, today):
    reservation = venue.reservations_for(maya)[1]
    assert reservation.event == jazz

    venue.refund(reservation, today)

    assert reservation.status == 'refunded'
    assert venue.seats_left(jazz) == 40


def test_a_refund_after_the_window_closes_is_refused_and_changes_nothing(venue, maya, jazz, capsys):
    reservation = venue.reservations_for(maya)[1]
    late = jazz.date - timedelta(days=3)

    venue.refund(reservation, late)

    assert reservation.status == 'paid'
    assert venue.seats_left(jazz) == 39
    assert capsys.readouterr().out == 'Refunds for Friday Night Jazz are closed.\n'


def test_refunding_an_unpaid_reservation_is_refused(venue, jordan, pottery, today, capsys):
    reservation = venue.reservations_for(jordan)[0]
    assert reservation.event == pottery

    venue.refund(reservation, today)

    assert reservation.status == 'reserved'
    assert capsys.readouterr().out == f'Cannot refund: reservation #{reservation.number} is reserved.\n'


def test_reservations_for_returns_only_that_attendees_reservations(venue, maya, jordan):
    assert len(venue.reservations_for(maya)) == 2
    assert len(venue.reservations_for(jordan)) == 2


def test_a_screening_is_never_refunded(venue, jordan, spirited_away, today, capsys):
    reservation = venue.reservations_for(jordan)[1]
    assert reservation.event == spirited_away

    venue.refund(reservation, today)

    assert reservation.status == 'paid'
    assert capsys.readouterr().out == 'Refunds for Movie Night: Spirited Away are closed.\n'
