# Passing the Function, Not Its Result: Python works out every argument before it calls a function.
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


def is_free(event):
    return event.ticket_price() == 0


print(hall.find_events(is_free))     # [Event('Board Game Night', 2027-01-08)]


# # ---------- Calling the callback too early ----------
# # Uncomment the line below on its own and run the file. Then comment it out again.

# # hall.find_events(is_free())   # crashes on purpose


# # ---------- Predict, then run ----------
# # This time the callback is called with an argument, so no argument is missing. What happens?
# # Uncomment the second line on its own and run the file. Then comment it out again.

board_games = hall.events[3]
# # hall.find_events(is_free(board_games))   # crashes on purpose
