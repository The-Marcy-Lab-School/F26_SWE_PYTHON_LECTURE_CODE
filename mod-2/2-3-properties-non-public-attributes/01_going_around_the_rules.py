# Going Around the Rules: assigning to an attribute runs no code in the class, so nothing can refuse it.
# Uncomment one section at a time as the lesson goes on.

from datetime import date


class Event:
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price
        self.seats_sold = 0

    def seats_left(self):
        return self.capacity - self.seats_sold

    def sell_ticket(self):
        if self.seats_left() == 0:
            print(f'{self.name} is sold out.')
            return
        self.seats_sold += 1


pottery = Event('Intro to Pottery', date(2026, 11, 20), 2, 15)
pottery.sell_ticket()
pottery.sell_ticket()
pottery.sell_ticket()        # Intro to Pottery is sold out.


# # ---------- Changing the Seat Count Directly ----------
# # This line never runs sell_ticket(), so the sold-out check never runs either.

# pottery.seats_sold += 1
# print(pottery.seats_left())   # -1


# # ---------- Assigning a Wrong Value Directly ----------
# # A staff member types 0 when they meant 10. Nothing refuses it, and the mistake shows up later.

# pottery = Event('Intro to Pottery', date(2026, 11, 20), 2, 15)
# pottery.sell_ticket()
# pottery.sell_ticket()
#
# pottery.capacity = 0
# pottery.sell_ticket()
# print(pottery.seats_left())   # -3
#
# # # A wrong capacity from the start is accepted too:
# empty = Event('Intro to Pottery', date(2026, 11, 20), 0, 15)
# print(empty.capacity)         # 0
