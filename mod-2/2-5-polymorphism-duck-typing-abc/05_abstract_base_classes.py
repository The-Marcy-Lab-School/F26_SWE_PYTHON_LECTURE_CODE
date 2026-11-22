# Abstract Base Classes: write the contract as code, so Python refuses an incomplete kind of event when it is created.
# Uncomment one section at a time as the lesson goes on.

from abc import ABC, abstractmethod
from datetime import date, timedelta


# ---------- Without an Abstract Base Class ----------
# A subclass that forgets an override is created and used without complaint, and gives a wrong answer.
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


class MidnightConcert(Event):
    # Meant to charge the $5 service fee, but its author forgot ticket_price()
    def __init__(self, name, date, capacity, base_price, performer):
        super().__init__(name, date, capacity, base_price)
        self.performer = performer


late_set = MidnightConcert('Midnight Set', date(2026, 12, 19), capacity=40, base_price=25, performer='Lena Ortiz')
print(late_set.ticket_price())   # 25, not 30: Event's version, with no service fee


# # ---------- With an Abstract Base Class ----------
# # Event inherits from ABC, and @abstractmethod marks the two methods every kind of event must define.

# # Contract: every kind of event defines
# #   ticket_price()      the price of one ticket
# #   can_refund(today)   whether a ticket can still be refunded on that day
class Event(ABC):
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price

    @abstractmethod
    def ticket_price(self):
        return self.base_price

    @abstractmethod
    def can_refund(self, today):
        pass


class Concert(Event):
    SERVICE_FEE = 5

    def __init__(self, name, date, capacity, base_price, performer):
        super().__init__(name, date, capacity, base_price)
        self.performer = performer

    def ticket_price(self):
        return super().ticket_price() + Concert.SERVICE_FEE

    def can_refund(self, today):
        return today <= self.date - timedelta(days=7)


class Festival(Event):
    # Forgot can_refund()
    def ticket_price(self):
        return super().ticket_price()


jazz = Concert('Friday Night Jazz', date(2026, 12, 5), capacity=40, base_price=25, performer='The Blue Notes')
# print(jazz.ticket_price())   # 30: Concert defines both methods, so it is a concrete class
#
# # Festival('Summer Festival', date(2026, 12, 10), capacity=500, base_price=40)  # crashes on purpose: TypeError
# # Event('Open Mic', date(2026, 12, 10), capacity=20, base_price=0)  # crashes on purpose: TypeError


# # ---------- Predict, then run ----------
# # With Event as an abstract base class, a screening is written the way it was before, defining only can_refund().
# # What happens when the program creates one? This one ends in an error: comment those lines out again before you go on.

class Screening(Event):
    def can_refund(self, today):
        return False


# coco = Screening('Movie Night: Coco', date(2026, 12, 18), capacity=30, base_price=8)


# # ---------- Abstract Base Class or Duck Typing? ----------
# # An abstract base class only checks classes that inherit from it. Duck typing accepts any class that defines the methods.

class MuseumTour:
    def __init__(self, name, date, price):
        self.name = name
        self.date = date
        self.price = price

    def ticket_price(self):
        return self.price

    def can_refund(self, today):
        return today < self.date


gallery = MuseumTour('Gallery After Dark', date(2026, 12, 11), price=12)
# print(gallery.ticket_price())   # 12: duck typing accepts any class that defines the method
#
# # Festival('Summer Festival', date(2026, 12, 10), capacity=500, base_price=40)  # crashes on purpose: TypeError
