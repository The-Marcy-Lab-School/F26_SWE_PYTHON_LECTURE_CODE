"""Sample data, so there is something on screen the first time you run the app
and the tests have data to test on"""

from datetime import timedelta

from attendee import Attendee
from events import Concert, Workshop, Screening
from venue import Venue


# Every date is set relative to `today`, so the sample events are always in the
# future (apart from one that has deliberately already happened). The tests pass
# in a fixed date, so they give the same result whatever day they run on.
def build_sample_venue(today):
    venue = Venue('Riverside Community Hall')

    jazz = Concert('Friday Night Jazz', today + timedelta(days=12),
                   capacity=40, base_price=25, performer='The Blue Notes')
    pottery = Workshop('Intro to Pottery', today + timedelta(days=4),
                       capacity=2, base_price=15, materials_fee=10)
    spirited_away = Screening('Movie Night: Spirited Away', today + timedelta(days=20),
                              capacity=30, base_price=8)
    coco = Screening('Movie Night: Coco', today - timedelta(days=5),
                     capacity=30, base_price=8)

    venue.add_event(jazz)
    venue.add_event(pottery)
    venue.add_event(spirited_away)
    venue.add_event(coco)

    maya = Attendee('Maya Rodriguez', 'maya@example.com')
    jordan = Attendee('Jordan Lee', 'jordan@example.com')
    venue.add_attendee(maya)
    venue.add_attendee(jordan)

    # The pottery workshop has two seats and two reservations, so it starts sold out
    maya_pottery = venue.book(maya, pottery, today)
    maya_pottery.pay()
    venue.book(jordan, pottery, today)

    maya_jazz = venue.book(maya, jazz, today)
    maya_jazz.pay()

    # Screenings are never refunded, so refunding this one shows a refusal
    jordan_movie = venue.book(jordan, spirited_away, today)
    jordan_movie.pay()

    return venue
