# ---------- Challenge: Events by Month 🏗️🏗️🏗️🏗️🏗️ ----------
# Finish events_in_month(month) so that it returns a new list of the venue's events
# whose date falls in that month, where month is a number from 1 to 12.
# Run the file after each step. It runs before you start, and prints nothing until the method is done:
#     python3 02_events_by_month.py

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

    def events_in_month(self, month):
        return []  # replace with a new list of the events in this month


hall = Venue('Riverside Community Hall')
hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), 40))
hall.add_event(Event('Intro to Pottery', date(2026, 12, 9), 12))
hall.add_event(Event('Holiday Crafts', date(2026, 12, 5), 15))
hall.add_event(Event('New Year Concert', date(2027, 1, 2), 60))

for event in hall.events_in_month(12):
    print(event.name)
# should print:
# Friday Night Jazz
# Intro to Pottery
# Holiday Crafts

for event in hall.events_in_month(1):
    print(event.name)
# should print:
# New Year Concert

print(len(hall.events_in_month(7)))  # should print 0
