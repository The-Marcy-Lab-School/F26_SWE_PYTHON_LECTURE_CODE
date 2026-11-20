# Two Searches, Written Twice: two search methods on Venue that differ only in their test.

from datetime import date


class Event:
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price

    def ticket_price(self):
        return self.base_price

    def __repr__(self):
        return f'Event({self.name!r}, {self.date})'


class Venue:
    def __init__(self, name):
        self.name = name
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def events_in_month(self, month):
        return [event for event in self.events if event.date.month == month]

    def events_under(self, price):
        return [event for event in self.events if event.ticket_price() < price]


hall = Venue('Riverside Community Hall')
hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), capacity=40, base_price=25))
hall.add_event(Event('Intro to Pottery', date(2026, 12, 9), capacity=12, base_price=15))
hall.add_event(Event('Movie Night: Coco', date(2026, 11, 28), capacity=30, base_price=8))
hall.add_event(Event('Board Game Night', date(2027, 1, 8), capacity=25, base_price=0))

print(hall.events_in_month(12))   # [Event('Friday Night Jazz', 2026-12-05), Event('Intro to Pottery', 2026-12-09)]
print(hall.events_under(10))      # [Event('Movie Night: Coco', 2026-11-28), Event('Board Game Night', 2027-01-08)]

# Q: Which parts of the two search methods are the same, and which part is different?
