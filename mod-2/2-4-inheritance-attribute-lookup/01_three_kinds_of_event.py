# Three Kinds of Event: a concert and a workshop written as separate classes, using only what you know so far.
# Which lines are the same in both classes, and which are different?

from datetime import date, timedelta


class Concert:
    def __init__(self, name, date, capacity, base_price, performer):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price
        self.performer = performer

    def ticket_price(self):
        return self.base_price + 5

    def can_refund(self, today):
        return today <= self.date - timedelta(days=7)

    def __repr__(self):
        return f'Concert({self.name!r}, {self.date})'

    def __eq__(self, other):
        return self.name == other.name and self.date == other.date


class Workshop:
    def __init__(self, name, date, capacity, base_price, materials_fee):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price
        self.materials_fee = materials_fee

    def ticket_price(self):
        return self.base_price + self.materials_fee

    def can_refund(self, today):
        return today <= self.date - timedelta(days=2)

    def __repr__(self):
        return f'Workshop({self.name!r}, {self.date})'

    def __eq__(self, other):
        return self.name == other.name and self.date == other.date


jazz = Concert('Friday Night Jazz', date(2026, 12, 5), capacity=40, base_price=25, performer='The Blue Notes')
pottery = Workshop('Intro to Pottery', date(2026, 12, 9), capacity=12, base_price=15, materials_fee=10)

print(jazz.ticket_price())      # 30
print(pottery.ticket_price())   # 25

# timedelta(days=7) is a length of time. Subtracting it from a date gives the date one week earlier,
# so self.date - timedelta(days=7) is the last day a concert ticket can be refunded.
print(jazz.date - timedelta(days=7))   # 2026-11-28
