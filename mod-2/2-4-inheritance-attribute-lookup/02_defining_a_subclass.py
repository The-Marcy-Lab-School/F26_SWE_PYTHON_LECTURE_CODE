# Defining a Subclass: the shared code lives in Event, and each kind of event writes only what is different.
# Uncomment one section at a time as the lesson goes on.

from datetime import date, timedelta


# ---------- Defining a Subclass ----------
# A subclass with nothing in its body receives every method of its superclass, including __init__.
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


class Screening(Event):
    pass


coco = Screening('Movie Night: Coco', date(2026, 12, 18), capacity=30, base_price=8)
print(coco.ticket_price())           # 8
print(isinstance(coco, Screening))   # True
print(isinstance(coco, Event))       # True


# # ---------- Predict, then run ----------
# # Screening has no __repr__ of its own, and the one it receives is written inside Event.
# # Does print(coco) show Event('Movie Night: Coco', 2026-12-18) or Screening('Movie Night: Coco', 2026-12-18)?

# print(coco)


# # ---------- Adding to a Subclass with super().__init__() ----------
# # Concert's own __init__ replaces Event's, so it runs Event's with super().__init__() and then stores the performer.

# class Concert(Event):
#     def __init__(self, name, date, capacity, base_price, performer):
#         super().__init__(name, date, capacity, base_price)
#         self.performer = performer
#
#
# jazz = Concert('Friday Night Jazz', date(2026, 12, 5), capacity=40, base_price=25, performer='The Blue Notes')
# print(jazz.name)        # Friday Night Jazz, stored by Event's __init__
# print(jazz.performer)   # The Blue Notes, stored by Concert's __init__


# # ---------- Predict, then run ----------
# # A concert ticket should cost its base price plus a $5 service fee.
# # Based on how Concert is currently written, what does jazz charge for a ticket?

# print(jazz.ticket_price())


# # ---------- Overriding a Method ----------
# # Screening tickets are never refunded. Screening's can_refund() overrides Event's, and Event's still runs for every other event.

# class Screening(Event):
#     def can_refund(self, today):
#         return False
#
#
# coco = Screening('Movie Night: Coco', date(2026, 12, 18), capacity=30, base_price=8)
# board_games = Event('Board Game Night', date(2026, 12, 18), capacity=25, base_price=5)
#
# print(coco.can_refund(date(2026, 12, 1)))          # False, from Screening's version
# print(board_games.can_refund(date(2026, 12, 1)))   # True, from Event's version


# # ---------- Check for understanding ----------
# # Suppose Screening's method had been misspelled when it was written.
# # What does coco.can_refund(date(2026, 12, 1)) return now, and why?

# class MisspelledScreening(Event):
#     def can_refunds(self, today):
#         return False
#
#
# coco = MisspelledScreening('Movie Night: Coco', date(2026, 12, 18), capacity=30, base_price=8)
# print(coco.can_refund(date(2026, 12, 1)))


# # ---------- Extending a Method with super() ----------
# # super().ticket_price() runs Event's version and hands back the base price, and Concert adds only the service fee.

# class Concert(Event):
#     def __init__(self, name, date, capacity, base_price, performer):
#         super().__init__(name, date, capacity, base_price)
#         self.performer = performer
#
#     def ticket_price(self):
#         return super().ticket_price() + 5
#
#     def can_refund(self, today):
#         return today <= self.date - timedelta(days=7)
#
#
# jazz = Concert('Friday Night Jazz', date(2026, 12, 5), capacity=40, base_price=25, performer='The Blue Notes')
# print(jazz.ticket_price())                     # 30: Event's 25, plus Concert's 5
# print(jazz.can_refund(date(2026, 11, 30)))     # False: refunds closed on November 28
