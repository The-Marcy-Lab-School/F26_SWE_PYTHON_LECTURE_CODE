# ---------- Challenge: A Workshop 🏗️🏗️🏗️🏗️🏗️ ----------
# Write Workshop as a subclass of Event:
# - its __init__ takes a fifth argument, materials_fee, and stores it;
# - its ticket_price() extends Event's version by adding the materials fee;
# - its can_refund() allows a refund until two days before the workshop.
# Run the file after each step:
#     python3 03_workshop.py
# Until Workshop has an __init__ that takes materials_fee, creating pottery stops the file with a TypeError.

from datetime import date, timedelta


class Event:
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price

    def ticket_price(self):
        return self.base_price

    def can_refund(self, today):
        return today < self.date

    def __repr__(self):
        return f'{type(self).__name__}({self.name!r}, {self.date})'

    def __eq__(self, other):
        return self.name == other.name and self.date == other.date


class Workshop(Event):
    pass


pottery = Workshop('Intro to Pottery', date(2026, 12, 9), capacity=12, base_price=15, materials_fee=10)
print(pottery)                                # should print Workshop('Intro to Pottery', 2026-12-09)
print(pottery.ticket_price())                 # should print 25
print(pottery.can_refund(date(2026, 12, 7)))  # should print True
print(pottery.can_refund(date(2026, 12, 8)))  # should print False
