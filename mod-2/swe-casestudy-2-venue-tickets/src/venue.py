"""The venue: the coordinator that owns every collection and enforces the venue's rules.

The venue refuses in two ways:
- An invalid value, such as a badly formed email address, raises a ValueError.
- An invalid action, such as booking a sold-out event, prints why and returns None.
"""

from reservation import Reservation


class Venue:
    def __init__(self, name):
        self.name = name
        self._events = []
        # A dictionary, so an attendee can be looked up by email in one step
        self._attendees = {}
        self._reservations = []
        # The venue issues reservation numbers, so every venue counts from 1001
        # and the new venue each test builds always starts at the same number
        self._next_number = 1001

    # Each collection can be read through a property. The property returns a new
    # list, so code outside the venue cannot add or remove anything without going
    # through the methods below, where the rules are checked.
    @property
    def events(self):
        return list(self._events)

    @property
    def attendees(self):
        return list(self._attendees.values())

    @property
    def reservations(self):
        return list(self._reservations)

    # A static method uses neither self nor cls. It is a plain function that
    # lives in the class because the venue is the only code that needs it.
    @staticmethod
    def is_valid_email(email):
        if '@' not in email:
            return False
        domain = email.split('@')[-1]
        return '.' in domain

    def add_event(self, event):
        # `in` compares with ==, which calls Event.__eq__, so an event built
        # again from the same name and date is found and refused
        if event in self._events:
            print(f'{event.name} on {event.date} is already on the calendar.')
            return None
        self._events.append(event)
        return event

    def add_attendee(self, attendee):
        if not Venue.is_valid_email(attendee.email):
            raise ValueError(f'"{attendee.email}" is not a valid email address.')
        if attendee.email in self._attendees:
            print(f'{attendee.email} is already registered.')
            return None
        self._attendees[attendee.email] = attendee
        return attendee

    def find_attendee(self, email):
        return self._attendees.get(email)

    # A higher-order method: `matches` is a function that takes one event and
    # returns True or False. The venue keeps every event it returns True for.
    def find_events(self, matches):
        return [event for event in self._events if matches(event)]

    def upcoming_events(self, today):
        upcoming = self.find_events(lambda event: event.date >= today)
        return sorted(upcoming, key=lambda event: event.date)

    def seats_left(self, event):
        taken = [reservation for reservation in self._reservations
                 if reservation.event == event and reservation.is_active()]
        return event.capacity - len(taken)

    def find_reservation(self, number):
        for reservation in self._reservations:
            if reservation.number == number:
                return reservation
        return None

    def reservations_for(self, attendee):
        return [reservation for reservation in self._reservations
                if reservation.attendee == attendee]

    def book(self, attendee, event, today):
        if event.date < today:
            print(f'{event.name} has already happened.')
            return None
        if self.seats_left(event) == 0:
            print(f'{event.name} is sold out.')
            return None
        reservation = Reservation(self._next_number, attendee, event)
        self._next_number += 1
        self._reservations.append(reservation)
        return reservation

    def refund(self, reservation, today):
        # The refund window is a venue rule that depends on today's date, so the
        # venue checks it before asking the reservation to change its status.
        # The reservation's own guard then checks that it has been paid.
        if not reservation.event.can_refund(today):
            print(f'Refunds for {reservation.event.name} are closed.')
            return
        reservation.refund()
