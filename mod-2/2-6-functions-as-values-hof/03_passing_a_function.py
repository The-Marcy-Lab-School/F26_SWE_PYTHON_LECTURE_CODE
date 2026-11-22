# Passing a Function to a Function: find_events() receives the test as a callback and calls it on each event.
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


def is_in_december(event):
    return event.date.month == 12


def is_free(event):
    return event.ticket_price() == 0


print(hall.find_events(is_in_december))   # [Event('Friday Night Jazz', 2026-12-05), Event('Intro to Pottery', 2026-12-09)]
print(hall.find_events(is_free))          # [Event('Board Game Night', 2027-01-08)]


# # ---------- Predict, then run ----------
# # This version of the test prints a line every time it runs. What does the program print, and in what order?

def is_cheap(event):
    print(f'Checking {event.name}')
    return event.ticket_price() < 10


# cheap = hall.find_events(is_cheap)
# print([event.name for event in cheap])


# # ---------- Check for understanding ----------
# # For each call below, say whether it is a higher-order function, and if it is, which condition it meets:
# # it takes a function as an argument, or it returns a function.

board_games = hall.events[3]

# print(hall.find_events(is_free))   # 1.
# print(len(hall.events))            # 2.
# print(is_free(board_games))        # 3.


# # ---------- Challenge: Finding Attendees ----------
# # Add a list of attendees to Venue, an add_attendee(attendee) method, and a higher-order method
# # find_attendees(matches) that returns the attendees for whom matches returns True.
# # Then write the two named functions below so the two calls print what the comments show.

from dataclasses import dataclass


@dataclass
class Attendee:
    name: str
    email: str


class Venue:
    def __init__(self, name):
        self.name = name
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def find_events(self, matches):
        return [event for event in self.events if matches(event)]

    def add_attendee(self, attendee):
        return None

    def find_attendees(self, matches):
        return None


def uses_example_email(attendee):
    return None

def name_starts_with_s(attendee):
    return None


hall = Venue('Riverside Community Hall')
hall.add_attendee(Attendee('Maya Rodriguez', 'maya@example.com'))
hall.add_attendee(Attendee('Sam Lee', 'sam@school.edu'))
hall.add_attendee(Attendee('Mona Patel', 'mona@example.com'))

# print(hall.find_attendees(uses_example_email))
# # [Attendee(name='Maya Rodriguez', email='maya@example.com'), Attendee(name='Mona Patel', email='mona@example.com')]
# print(hall.find_attendees(name_starts_with_s))
# # [Attendee(name='Sam Lee', email='sam@school.edu')]
