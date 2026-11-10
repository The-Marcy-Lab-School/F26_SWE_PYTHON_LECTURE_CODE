# Non-Public Attributes and @property: a property lets the class take part when its data is read or assigned.
# Uncomment one section at a time as the lesson goes on.

from datetime import date


# ---------- Step 1. A Value Other Code Can Read but Not Assign ----------
# The seat count is stored under _seats_sold, and the seats_sold getter reads it.
class Event:
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price
        self._seats_sold = 0

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
pottery.sell_ticket()
print(pottery.seats_sold)      # Python runs the seats_sold getter, which returns self._seats_sold -> 1
print(pottery.seats_left())    # 1


# # ---------- Predict, then run ----------
# # The class defines how to read seats_sold and nothing else. What happens when code outside the class
# # tries to add a seat directly? This one ends in an error: comment the line out again before you go on.

# pottery = Event('Intro to Pottery', date(2026, 11, 20), 2, 15)
# pottery.seats_sold += 1


# # ---------- Check for understanding ----------
# # Suppose the last line of sell_ticket() were self.seats_sold += 1 instead of self._seats_sold += 1.
# # What happens on the first sale, and why does the original line work?
# # This one ends in an error too: comment the call out again before you go on.

# class BrokenEvent:
#     def __init__(self, name, date, capacity, base_price):
#         self.name = name
#         self.date = date
#         self.capacity = capacity
#         self.base_price = base_price
#         self._seats_sold = 0
#
#     @property
#     def seats_sold(self):
#         return self._seats_sold
#
#     def seats_left(self):
#         return self.capacity - self.seats_sold
#
#     def sell_ticket(self):
#         if self.seats_left() == 0:
#             print(f'{self.name} is sold out.')
#             return
#         self.seats_sold += 1
#
#
# broken = BrokenEvent('Intro to Pottery', date(2026, 11, 20), 2, 15)
# broken.sell_ticket()


# # ---------- Step 2. Refusing a Wrong Value with a Setter ----------
# # The setter runs every time something assigns to capacity, including the line in __init__.

# class Event:
#     def __init__(self, name, date, capacity, base_price):
#         self.name = name
#         self.date = date
#         self.capacity = capacity      # runs the setter below
#         self.base_price = base_price
#         self._seats_sold = 0
#
#     @property
#     def capacity(self):
#         return self._capacity
#
#     @capacity.setter
#     def capacity(self, value):
#         if value < 1:
#             raise ValueError(f'Capacity must be at least 1, not {value}.')
#         self._capacity = value
#
#     @property
#     def seats_sold(self):
#         return self._seats_sold
#
#     def seats_left(self):
#         return self.capacity - self.seats_sold
#
#     def sell_ticket(self):
#         if self.seats_left() == 0:
#             print(f'{self.name} is sold out.')
#             return
#         self._seats_sold += 1
#
#
# pottery = Event('Intro to Pottery', date(2026, 11, 20), 2, 15)
# pottery.capacity = 12         # a good capacity is accepted
# print(pottery.capacity)       # 12
#
# # pottery.capacity = 0  # crashes on purpose: ValueError: Capacity must be at least 1, not 0.


# # ---------- Predict, then run ----------
# # What happens when the event is created with a capacity of 0?
# # This one ends in an error: comment the lines out again before you go on.

# pottery = Event('Intro to Pottery', date(2026, 11, 20), 0, 15)
# print(pottery.name)
