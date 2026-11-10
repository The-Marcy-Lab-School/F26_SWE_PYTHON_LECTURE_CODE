# ---------- Challenge: One Ticket per Attendee 🏗️🏗️🏗️🏗️🏗️ ----------
# Give Venue a list of reservations, and finish book(attendee, event) so that it creates a Reservation,
# adds it to the list, and returns it. An attendee may hold only one ticket for an event, so book() must refuse
# a second reservation for the same attendee and event: it prints
# "<attendee's name> already has a ticket for <event's name>.", adds nothing, and returns None.
# Run the file after each step. It runs before you start, and prints [] until book() is done:
#     python3 08_one_ticket_per_attendee.py

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


@dataclass
class Attendee:
    name: str
    email: str


@dataclass
class Reservation:
    attendee: Attendee
    event: Event


class Venue:
    def __init__(self, name):
        self.name = name
        self.events = []
        self.reservations = []

    def add_event(self, event):
        if event in self.events:
            print(f'{event.name} on {event.date} is already on the calendar.')
            return
        self.events.append(event)

    def book(self, attendee, event):
        return None  # replace with the reservation, or a refusal


hall = Venue('Riverside Community Hall')
jazz = Event('Friday Night Jazz', date(2026, 12, 5), 40)
hall.add_event(jazz)

hall.book(Attendee('Maya Rodriguez', 'maya@example.com'), jazz)
hall.book(Attendee('Maya Rodriguez', 'maya@example.com'), jazz)  # should print Maya Rodriguez already has a ticket for Friday Night Jazz.
hall.book(Attendee('Sam Lee', 'sam@example.com'), jazz)

print(hall.reservations)
# should print one reservation for Maya and one for Sam:
# [Reservation(attendee=Attendee(name='Maya Rodriguez', email='maya@example.com'), event=Event('Friday Night Jazz', 2026-12-05)), Reservation(attendee=Attendee(name='Sam Lee', email='sam@example.com'), event=Event('Friday Night Jazz', 2026-12-05))]
