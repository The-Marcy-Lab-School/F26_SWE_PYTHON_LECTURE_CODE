# Writing a Function Inline with lambda: a one-line callback written right where it is used.
# Uncomment one section at a time as the lesson goes on.

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


# The venue from Passing a Function to a Function: one search method that takes the test as a parameter
class Venue:
    def __init__(self, name):
        self.name = name
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def find_events(self, matches):
        return [event for event in self.events if matches(event)]


hall = Venue('Riverside Community Hall')
hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), capacity=40, base_price=25))
hall.add_event(Event('Intro to Pottery', date(2026, 12, 9), capacity=12, base_price=15))
hall.add_event(Event('Movie Night: Coco', date(2026, 11, 28), capacity=30, base_price=8))
hall.add_event(Event('Board Game Night', date(2027, 1, 8), capacity=25, base_price=0))


print(hall.find_events(lambda event: event.ticket_price() < 10))
# [Event('Movie Night: Coco', 2026-11-28), Event('Board Game Night', 2027-01-08)]

print(hall.find_events(lambda event: 'Night' in event.name))
# [Event('Friday Night Jazz', 2026-12-05), Event('Movie Night: Coco', 2026-11-28), Event('Board Game Night', 2027-01-08)]


# # ---------- Check for understanding ----------
# # Rewrite each search as a single call to hall.find_events() with a lambda, in place of the None below.

# capacity_30_or_more = None   # 1. The events with a capacity of 30 or more
# in_2027 = None               # 2. The events that take place in 2027
#
# print(capacity_30_or_more)
# # [Event('Friday Night Jazz', 2026-12-05), Event('Movie Night: Coco', 2026-11-28)]
# print(in_2027)
# # [Event('Board Game Night', 2027-01-08)]
