# Putting It Together: Reservations. A reservation holds an attendee and an event.
# Uncomment one section at a time as the lesson goes on.

from dataclasses import dataclass
from datetime import date


class Event:
    def __init__(self, name, date, capacity):
        self.name = name
        self.date = date
        self.capacity = capacity

    def __repr__(self):
        return f'Event({self.name!r}, {self.date})'

    def __eq__(self, other):
        return self.name == other.name and self.date == other.date


class Venue:
    def __init__(self, name):
        self.name = name
        self.events = []

    def add_event(self, event):
        if event in self.events:
            print(f'{event.name} on {event.date} is already on the calendar.')
            return
        self.events.append(event)


@dataclass
class Attendee:
    name: str
    email: str


@dataclass
class Reservation:
    attendee: Attendee
    event: Event


# # ---------- Predict, then run ----------
# # What do the four print() calls show?

# hall = Venue('Riverside Community Hall')
# hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), 40))
#
# maya = Attendee('Maya Rodriguez', 'maya@example.com')
# first = Reservation(maya, hall.events[0])
# print(first)
# print(first.attendee.name)
#
# second = Reservation(Attendee('Maya Rodriguez', 'maya@example.com'),
#                      Event('Friday Night Jazz', date(2026, 12, 5), 60))
# print(first == second)
# print(first.event is hall.events[0])
