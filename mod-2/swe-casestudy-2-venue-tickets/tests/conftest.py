"""Shared setup for every test."""

from datetime import date

import pytest

from sample_data import build_sample_venue


# A fixed date, so the tests give the same result whatever day they run on
@pytest.fixture
def today():
    return date(2026, 12, 1)


# A new venue for every test, so a change made by one test never reaches the next
@pytest.fixture
def venue(today):
    return build_sample_venue(today)


@pytest.fixture
def jazz(venue):
    return venue.find_events(lambda event: event.name == 'Friday Night Jazz')[0]


@pytest.fixture
def pottery(venue):
    return venue.find_events(lambda event: event.name == 'Intro to Pottery')[0]


@pytest.fixture
def spirited_away(venue):
    return venue.find_events(lambda event: event.name == 'Movie Night: Spirited Away')[0]


@pytest.fixture
def coco(venue):
    return venue.find_events(lambda event: event.name == 'Movie Night: Coco')[0]


@pytest.fixture
def maya(venue):
    return venue.find_attendee('maya@example.com')


@pytest.fixture
def jordan(venue):
    return venue.find_attendee('jordan@example.com')
