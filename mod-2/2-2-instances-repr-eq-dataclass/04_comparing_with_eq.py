# Comparing Instances with __eq__: in checks each element with ==, and == calls __eq__.
# Uncomment one section at a time as the lesson goes on.

from datetime import date


class Event:
    def __init__(self, name, date, capacity):
        self.name = name
        self.date = date
        self.capacity = capacity

    def __repr__(self):
        return f'Event({self.name!r}, {self.date})'


class Venue:
    def __init__(self, name):
        self.name = name
        self.events = []

    def add_event(self, event):
        if event in self.events:
            print(f'{event.name} on {event.date} is already on the calendar.')
            return
        self.events.append(event)


# A first attempt at refusing a duplicate: the check never prints its message
hall = Venue('Riverside Community Hall')
hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), 40))
hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), 40))

print(hall.events)
# [Event('Friday Night Jazz', 2026-12-05), Event('Friday Night Jazz', 2026-12-05)]

# Without __eq__, == checks identity, the same question is asks
jazz = Event('Friday Night Jazz', date(2026, 12, 5), 40)
jazz_again = Event('Friday Night Jazz', date(2026, 12, 5), 40)

print(jazz == jazz_again)   # False
print(jazz is jazz_again)   # False


# # ---------- Writing __eq__ ----------
# # Two events that share a name and a date are equal.

# class Event:
#     def __init__(self, name, date, capacity):
#         self.name = name
#         self.date = date
#         self.capacity = capacity
#
#     def __repr__(self):
#         return f'Event({self.name!r}, {self.date})'
#
#     def __eq__(self, other):
#         return self.name == other.name and self.date == other.date
#
#
# jazz = Event('Friday Night Jazz', date(2026, 12, 5), 40)
# jazz_again = Event('Friday Night Jazz', date(2026, 12, 5), 40)
#
# print(jazz == jazz_again)   # Python calls jazz.__eq__(jazz_again) -> True: same name, same date
# print(jazz is jazz_again)   # False: still two separate objects
#
# # # in uses ==, so the venue now refuses the second concert:
# hall = Venue('Riverside Community Hall')
# hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), 40))
# hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), 40))
# # Friday Night Jazz on 2026-12-05 is already on the calendar.
#
# print(hall.events)
# # [Event('Friday Night Jazz', 2026-12-05)]
#
# # # Predict, then run: the concert typed in again with a capacity of 60, then a second concert a week later.
# # # What does each call print, and how many events does the venue hold at the end?
# hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), 60))
# hall.add_event(Event('Friday Night Jazz', date(2026, 12, 12), 40))
# print(len(hall.events))
