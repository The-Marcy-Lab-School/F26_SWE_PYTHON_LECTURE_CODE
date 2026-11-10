# Objects That Hold Other Objects: a venue holds a list of events.
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


hall = Venue('Riverside Community Hall')
jazz = Event('Friday Night Jazz', date(2026, 12, 5), 40)
pottery = Event('Intro to Pottery', date(2026, 12, 9), 12)
hall.add_event(jazz)
hall.add_event(pottery)

# You will often see classes instantiated directly in a method call like this
hall.add_event(Event('Holiday Crafts', date(2026, 12, 5), 15))


# # ---------- Reaching Through One Object to Another ----------
# # Write one step for each object you pass through.

# print(hall.events[0].name)         # Friday Night Jazz
# print(hall.events[1].date.month)   # 12
#
# # # Predict, then run: the jazz concert moves to a bigger room. What do the two print() calls show?
# jazz.capacity = 60
#
# print(hall.events[0].capacity)
# print(jazz is hall.events[0])


# # ---------- A Method That Searches the List ----------
# # The venue holds the list, so the venue is the natural place for code that searches it.

# class Venue:
#     def __init__(self, name):
#         self.name = name
#         self.events = []
#
#     def add_event(self, event):
#         self.events.append(event)
#
#     def events_on(self, day):
#         return [event for event in self.events if event.date == day]
#
#
# hall = Venue('Riverside Community Hall')
# hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), 40))
# hall.add_event(Event('Intro to Pottery', date(2026, 12, 9), 12))
# hall.add_event(Event('Holiday Crafts', date(2026, 12, 5), 15))
#
# for event in hall.events_on(date(2026, 12, 5)):
#     print(event.name)
# # Friday Night Jazz
# # Holiday Crafts
#
# print(len(hall.events_on(date(2026, 12, 25))))  # 0
