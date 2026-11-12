"""Tests for the Reservation class and its status guards."""

import pytest


def test_each_new_reservation_gets_the_next_number(venue, jordan, jazz, today):
    # The sample venue has already made reservations 1001 to 1004
    reservation = venue.book(jordan, jazz, today)

    assert reservation.number == 1005


def test_a_new_reservation_starts_reserved(venue, jordan, jazz, today):
    reservation = venue.book(jordan, jazz, today)

    assert reservation.status == 'reserved'


def test_the_price_is_fixed_when_the_reservation_is_made(venue, jordan, jazz, today):
    reservation = venue.book(jordan, jazz, today)

    jazz.base_price = 100

    assert reservation.price == 30


def test_paying_moves_a_reservation_to_paid(venue, jordan, jazz, today):
    reservation = venue.book(jordan, jazz, today)

    reservation.pay()

    assert reservation.status == 'paid'


def test_checking_in_before_paying_is_refused(venue, jordan, jazz, today, capsys):
    reservation = venue.book(jordan, jazz, today)

    reservation.check_in()

    assert reservation.status == 'reserved'
    assert capsys.readouterr().out == f'Cannot check_in: reservation #{reservation.number} is reserved.\n'


def test_paying_twice_is_refused(venue, jordan, jazz, today, capsys):
    reservation = venue.book(jordan, jazz, today)
    reservation.pay()

    reservation.pay()

    assert reservation.status == 'paid'
    assert capsys.readouterr().out == f'Cannot pay: reservation #{reservation.number} is paid.\n'


def test_the_status_cannot_be_assigned_directly(venue, jordan, jazz, today):
    reservation = venue.book(jordan, jazz, today)

    with pytest.raises(AttributeError):
        reservation.status = 'checked_in'

    assert reservation.status == 'reserved'
