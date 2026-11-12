"""Tests for the Attendee dataclass."""

from attendee import Attendee


def test_two_attendees_with_the_same_data_are_equal():
    assert Attendee('Maya Rodriguez', 'maya@example.com') == Attendee('Maya Rodriguez', 'maya@example.com')


def test_the_dataclass_writes_a_readable_repr():
    attendee = Attendee('Maya Rodriguez', 'maya@example.com')

    assert repr(attendee) == "Attendee(name='Maya Rodriguez', email='maya@example.com')"
