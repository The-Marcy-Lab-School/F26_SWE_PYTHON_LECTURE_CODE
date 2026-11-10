from datetime import date

from venue import Event, Venue


def test_adding_an_equal_event_again_is_refused():
    hall = Venue('Riverside Community Hall')
    hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), 40))

    hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), 40))

    assert len(hall.events) == 1


def test_an_event_on_another_day_is_added():
    hall = Venue('Riverside Community Hall')
    hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), 40))

    hall.add_event(Event('Friday Night Jazz', date(2026, 12, 12), 40))

    assert len(hall.events) == 2
