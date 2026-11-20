# Advanced Topics: map() and filter(), sorting by two values, a dictionary of functions, and nonlocal.
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


# # ---------- map() and filter() ----------

# cheap = list(filter(lambda event: event.ticket_price() < 10, hall.events))
# names = list(map(lambda event: event.name, cheap))
# print(names)   # ['Movie Night: Coco', 'Board Game Night']
#
# names = [event.name for event in hall.events if event.ticket_price() < 10]
# print(names)   # ['Movie Night: Coco', 'Board Game Night']


# # ---------- Sorting by More Than One Value ----------

# hall.add_event(Event('Holiday Crafts', date(2026, 12, 5), capacity=15, base_price=10))
#
# by_day_then_name = sorted(hall.events, key=lambda event: (event.date, event.name))
# print([event.name for event in by_day_then_name])
# # ['Movie Night: Coco', 'Friday Night Jazz', 'Holiday Crafts', 'Intro to Pottery', 'Board Game Night']


# # ---------- A Dictionary of Functions in Place of an if/elif Chain ----------

# def list_events(venue):
#     print([event.name for event in venue.events])
#
# def count_events(venue):
#     print(len(venue.events))
#
# actions = {'1': list_events, '2': count_events}
#
# choice = '2'
# actions[choice](hall)   # 5 once the section above has added Holiday Crafts, or 4 without it


# # ---------- Changing a Closed-Over Variable with nonlocal ----------
# # Uncomment the door() line on its own to see the error, then comment it out again.

# def make_counter():
#     count = 0
#     def counter():
#         count += 1
#         return count
#     return counter
#
#
# door = make_counter()
# # door()   # crashes on purpose
#
#
# def make_counter():
#     count = 0
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter
#
#
# door = make_counter()
# box_office = make_counter()
# print(door(), door(), box_office(), door())   # 1 2 1 3
