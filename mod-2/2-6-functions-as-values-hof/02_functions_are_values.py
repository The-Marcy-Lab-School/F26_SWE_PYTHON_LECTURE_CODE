# Functions Are Values: a function's name without parentheses is the function itself; with parentheses it is a call.
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


board_games = hall.events[3]

print(type(is_free))         # <class 'function'>
print(is_free)               # <function is_free at 0x...>: the function itself
print(is_free(board_games))  # True: the value the call returned

check = is_free              # a second name for the same function; nothing is called
print(check(board_games))    # True


# # ---------- Pop quiz! Name the data type stored in each variable ----------
# # Write down your answer for each variable first, then run the section to check.

# a = 'Friday Night Jazz'
# b = 40
# c = True
# d = ['A1', 'A2']
# e = {'Main Hall': 150}
#
# def f(event):
#     return event.ticket_price() == 0
#
# for value in [a, b, c, d, e, f]:
#     print(type(value))


# # ---------- Predict, then run ----------
# # The venue's announcements can be printed in two styles, and each style is a function stored in a dictionary.
# # What do the two print() calls show?

# def shout(message):
#     return message.upper()
#
# def whisper(message):
#     return message.lower()
#
# styles = {'shout': shout, 'whisper': whisper}
#
# print(styles['shout']('Doors open at 7'))
# print(styles['whisper'])
