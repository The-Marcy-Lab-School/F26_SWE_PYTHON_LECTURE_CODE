# The Underscore Is a Convention: Python lets any code reach an attribute whose name starts with an underscore.
# Uncomment one section at a time as the lesson goes on.

from datetime import date


class Event:
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price
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


# The assignment goes straight to the stored value and skips the setter, so the check never runs
pottery = Event('Intro to Pottery', date(2026, 11, 20), 2, 15)
pottery._capacity = -5            # no error
print(pottery.seats_left())       # -5


# # ---------- Going Through the Property ----------
# # Code outside the class should use pottery.capacity, where the rule is checked.

# pottery = Event('Intro to Pottery', date(2026, 11, 20), 2, 15)
# # pottery.capacity = -5  # crashes on purpose: ValueError: Capacity must be at least 1, not -5.
# print(pottery.capacity)           # 2
