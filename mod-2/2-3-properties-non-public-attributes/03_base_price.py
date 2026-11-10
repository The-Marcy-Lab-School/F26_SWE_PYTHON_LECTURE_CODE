# ---------- Challenge: Base Price 🏗️🏗️🏗️🏗️🏗️ ----------
# Give Event a base_price property:
# - store the price under _base_price, and add a getter that returns it;
# - add a setter that refuses a negative price by raising a ValueError whose message names the rule
#   and the refused value, such as "A price cannot be negative, not -15.";
# - make __init__ run the setter. A price of 0 is allowed, because the venue runs free events.
# Run the file after each step. It runs before you start, and prints -15 at the end until your setter refuses it:
#     python3 03_base_price.py

from datetime import date


class Event:
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price  # make this line run your setter
        self._seats_sold = 0

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 1:
            raise ValueError(f'Capacity must be at least 1, not {value}.')
        self._capacity = value

    @property
    def seats_sold(self):
        return self._seats_sold

    def seats_left(self):
        return self.capacity - self.seats_sold

    def sell_ticket(self):
        if self.seats_left() == 0:
            print(f'{self.name} is sold out.')
            return
        self._seats_sold += 1


pottery = Event('Intro to Pottery', date(2026, 11, 20), 2, 15)
pottery.base_price = 20
print(pottery.base_price)   # should print 20

pottery.base_price = 0
print(pottery.base_price)   # should print 0

pottery.base_price = -15    # should raise ValueError: A price cannot be negative, not -15.
print(pottery.base_price)   # should never run once your setter refuses -15
