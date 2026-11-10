from datetime import date

import pytest
from event import Event


def test_a_capacity_below_one_is_refused():
    pottery = Event('Intro to Pottery', date(2026, 11, 20), 2, 15)

    with pytest.raises(ValueError):
        pottery.capacity = 0


def test_a_refused_capacity_leaves_the_stored_value_unchanged():
    pottery = Event('Intro to Pottery', date(2026, 11, 20), 2, 15)

    with pytest.raises(ValueError):
        pottery.capacity = 0

    assert pottery.capacity == 2
