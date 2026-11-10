# Printing an Instance with __repr__: print() shows whatever __repr__ returns.
# Uncomment one section at a time as the lesson goes on.

from datetime import date


class Event:
    def __init__(self, name, date, capacity):
        self.name = name
        self.date = date
        self.capacity = capacity


class Venue:
    def __init__(self, name):
        self.name = name
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def events_on(self, day):
        return [event for event in self.events if event.date == day]


hall = Venue('Riverside Community Hall')
hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), 40))
hall.add_event(Event('Holiday Crafts', date(2026, 12, 5), 15))

# The class and a memory address, but not which event
print(hall.events_on(date(2026, 12, 5)))
# [<__main__.Event object at 0x1027ddfd0>, <__main__.Event object at 0x1027bc410>]


# # ---------- __repr__ ----------
# # Python calls __repr__ whenever it needs to show an object to a programmer.

# class Event:
#     def __init__(self, name, date, capacity):
#         self.name = name
#         self.date = date
#         self.capacity = capacity
#
#     def __repr__(self):
#         return f'Event({self.name!r}, {self.date})'
#
#
# hall = Venue('Riverside Community Hall')
# hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), 40))
# hall.add_event(Event('Holiday Crafts', date(2026, 12, 5), 15))
#
# print(hall.events[0])     # Event('Friday Night Jazz', 2026-12-05)
# print(hall.events)        # [Event('Friday Night Jazz', 2026-12-05), Event('Holiday Crafts', 2026-12-05)]
#
# # # !r shows a value the way it would be written in code, so a string gets quotes:
# print(f'{hall.events[0].name}')     # Friday Night Jazz
# print(f'{hall.events[0].name!r}')   # 'Friday Night Jazz'


# # ---------- A __repr__ That Prints Instead of Returning ----------
# # __repr__ must return its string. This one prints it and hands back None.

# class BrokenEvent:
#     def __init__(self, name, date):
#         self.name = name
#         self.date = date
#
#     def __repr__(self):
#         print(f'Event({self.name!r}, {self.date})')    # prints instead of returning
#
#
# broken = BrokenEvent('Friday Night Jazz', date(2026, 12, 5))
# # print([broken])  # crashes on purpose: TypeError: __repr__ returned non-string (type NoneType)
