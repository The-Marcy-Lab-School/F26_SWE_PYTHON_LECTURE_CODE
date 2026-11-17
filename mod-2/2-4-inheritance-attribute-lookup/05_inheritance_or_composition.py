# Inheritance or Composition? "Is a" means one class inherits from another, and "has a" means one object holds another.

from dataclasses import dataclass
from datetime import date


class Event:
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price

    def __repr__(self):
        return f'{type(self).__name__}({self.name!r}, {self.date})'


class Concert(Event):          # a concert is an event
    def __init__(self, name, date, capacity, base_price, performer):
        super().__init__(name, date, capacity, base_price)
        self.performer = performer


@dataclass
class Attendee:
    name: str
    email: str


@dataclass
class Reservation:             # a reservation has an attendee and an event
    attendee: Attendee
    event: Event


jazz = Concert('Friday Night Jazz', date(2026, 12, 5), capacity=40, base_price=25, performer='The Blue Notes')
maya = Attendee('Maya Rodriguez', 'maya@example.com')
ticket = Reservation(maya, jazz)

print(isinstance(jazz, Event))       # True: a concert is an event
print(isinstance(ticket, Event))     # False: a reservation is not an event
print(ticket.event is jazz)          # True: the reservation holds the concert itself
print(ticket.event.performer)        # The Blue Notes
